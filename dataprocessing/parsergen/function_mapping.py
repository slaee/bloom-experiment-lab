import re
import sys

def detect_sql_vulnerability(code):
    sql_syntax_pattern = re.compile(r'\b(?:SELECT|INSERT|UPDATE|DELETE|FROM|WHERE|AND|OR)\b', re.IGNORECASE)
    sql_function_pattern = re.compile(r'\b(?:mysql_query|mysqli_query|pg_query|sqlite_query)\b', re.IGNORECASE)
    concatenated_string_pattern = re.compile(r'["\']\s*\.\s*["\']')

    sql_syntax_count = 1 if len(re.findall(sql_syntax_pattern, code)) > 0 else 0
    sql_function_count = 1 if len(re.findall(sql_function_pattern, code)) > 0 else 0
    concatenated_string_count = 1 if len(re.findall(concatenated_string_pattern, code)) > 0 else 0

    return sql_syntax_count, sql_function_count, concatenated_string_count

def detect_command_injection(code):
    html_tag_pattern = re.compile(r'<\s*(?:script|iframe|embed|object|applet)\b', re.IGNORECASE)
    concatenated_string_pattern = re.compile(r'["\']\s*\.\s*["\']')

    html_tag_count = 1 if len(re.findall(html_tag_pattern, code)) > 0 else 0
    concatenated_string_count = 1 if len(re.findall(concatenated_string_pattern, code)) > 0 else 0

    return html_tag_count, 0, concatenated_string_count

def detect_xss_vulnerability(code):
    system_call_pattern = re.compile(r'\b(?:exec|system|shell_exec|passthru)\b', re.IGNORECASE)
    invoked_function_pattern = re.compile(r'\b(?:eval|create_function)\b', re.IGNORECASE)
    concatenated_string_pattern = re.compile(r'["\']\s*\.\s*["\']')

    system_call_count = 1 if len(re.findall(system_call_pattern, code)) > 0 else 0
    invoked_function_count = 1 if len(re.findall(invoked_function_pattern, code)) > 0 else 0
    concatenated_string_count = 1 if len(re.findall(concatenated_string_pattern, code)) > 0 else 0

    return system_call_count, invoked_function_count, concatenated_string_count

def compute_combined_matrix(matrix):
    combined_matrix = [1 if any(row) else 0 for row in matrix]
    return combined_matrix

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]

    try:
        with open(filename, 'r') as file:
            code = file.read()

        sql_counts = detect_sql_vulnerability(code)
        command_counts = detect_command_injection(code)
        xss_counts = detect_xss_vulnerability(code)

        matrix = [
            list(sql_counts),
            list(command_counts),
            list(xss_counts)
        ]

        vulnerability_labels = ["SQL Vulnerability", "Command Injection", "XSS Vulnerability"]

        print("Vulnerability Matrix with Labels:")
        for label, row in zip(vulnerability_labels, matrix):
            print(f"{label}: {row}")

        print("\nX-Feature:")
        for row in matrix:
            print(row)

        print("\nY-Feature:")
        print(compute_combined_matrix(matrix))

    except FileNotFoundError:
        print(f"File not found: {filename}")

if __name__ == "__main__":
    main()