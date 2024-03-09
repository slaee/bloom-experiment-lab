import subprocess
import re
import sys

def run_get_vars_php(filename):
    result = subprocess.run(["php", "get_vars.php", filename], capture_output=True, text=True)
    return result.stdout

def parse_var_references(output):
    references_map = {}

    lines = output.splitlines()
    for line in lines:
        parts = line.strip().split(',')
        if len(parts) > 1:
            variable = parts[0]
            references = parts[1:]
            references_map[variable] = references

    return references_map

def get_line_references(filename, variable, references_map):
    with open(filename, 'r') as file:
        code = file.readlines()

    line_references = []
    for i, line in enumerate(code, start=1):
        for reference in references_map[variable]:
            if re.search(fr'\b{re.escape(reference)}\b', line):
                line_references.append(f'"{line.strip()}"')

    return line_references

def main():
    if len(sys.argv) != 2:
        print("Usage: python get_var_references.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]
    get_vars_output = run_get_vars_php(filename)
    references_map = parse_var_references(get_vars_output)

    for variable, references in references_map.items():
        line_references = []
        for reference in references:
            line_references.extend(get_line_references(filename, variable, references_map))

        references = [f'"{variable}"'] + line_references
        print(f'({", ".join(references)})')

if __name__ == "__main__":
    main()
