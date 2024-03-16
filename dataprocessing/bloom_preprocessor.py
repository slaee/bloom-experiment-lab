import subprocess
import os
import re
from pprint import pprint

js_getVARS_loc = os.path.join(os.path.abspath('parsergen'), "get_vars.js")
php_getVARS_loc = os.path.join(os.path.abspath('parsergen'), "get_vars.php")
php_samples_loc = os.path.join(os.path.abspath('parsergen'), "php_samples")
js_samples_loc = os.path.join(os.path.abspath('parsergen'), "js_samples")


def execute_getvars(file_loc, lang):
    if lang == "php":
        cmd = ["php", php_getVARS_loc, file_loc]
    elif lang == "js":
        cmd =  ["node", js_getVARS_loc, "module", file_loc]
    else:
        return "Invalid language"
    result = subprocess.check_output(cmd, stderr=subprocess.PIPE).decode('utf-8')
    return result

def code_cleaner(filename):
    with open(filename, 'r') as f:
        code = f.read()

    # GENERAL: 
    # remove multiline comments
    code = re.sub(r'/\*(.*?)\*/', '', code, flags=re.DOTALL)
    # remove all single line comments (//|#) except if (//|#) is inside of a string like "htes // asdf" or 'htes # asdf'
    code = re.sub(r'(?<!\\)(["\'])(?:\\.|(?!\1).)*?\1|//.*?$|#.*?$', 
                  lambda m: m.group(0) if m.group(0).startswith('"') or m.group(0).startswith("'") else '', code, flags=re.MULTILINE)
    # remove all newlines after a ( ,|.|\(|\[ ) or spaces after a ( ,|.|\(|\[ )
    code = re.sub(r'(\[|\(|,|\.)\s+', r'\1', code)
    # remove all newlines before a ( ,|.|;|\)|\] ) or spaces before a ( ,|.|;|\)|\] )
    code = re.sub(r'\s+(\]|\)|,|\.|;)', r'\1', code)
    # remove all trailing comma before a ( \) | \] )
    code = re.sub(r',(\s*[\]\)])', r'\1', code)
    # split code into lines
    code = code.split('\n')
    # remove leading and trailing whitespace
    code = [line.strip() for line in code]
    # remove all semi-colons at the end of a line
    code = [re.sub(r'(;|{)$', '', line).strip() for line in code]
    
    # After removing aliens, we can remove some twigs symbols, single words and numbers
    # remove all elements that are one word or numeric only in a string or symbols only in a string
    code = [line for line in code if not re.match(r'^\W+$', line) 
                                        and not re.match(r'^\w+$', line) 
                                            and not re.match(r'^\d+$', line)]

    # PHP:
    # remove all php tags
    code = [line for line in code if not line.startswith('<?php') and not line.startswith('?>')]

    # lastly remove all empty lines
    code = list(filter(None, code))

    return code

# Extract the variable references of JS and PHP
def extract_vars_references(vars, code):
    references = []
    for var in vars:
        # case sensitive and match whole word only or if wrapped in a special character
        var_pattern = r'(?<!\w)' + re.escape(var) + r'(?!\w)'
        
        var_references = []
        for line in code:
            if re.search(var_pattern, line):
                var_references.append(line)
        references.append((var, var_references))

    return references

def check_variable_usage(code_snippet):
    # php regex rules for catching tainted variables with user input
    php_pattern = re.compile(r'\b(?:php|http)://|(?:(\$_(?:GET|POST|REQUEST|SERVER|COOKIE|ENV|FILES)\b)|\b(?:GET|POST|REQUEST|SERVER|COOKIE|ENV|FILES)\b)\b')
    # pure js regex rules for catching tainted variables with user input
    js_pattern = re.compile(r'(?:req|request)\.(?:body|params|query|headers)', re.IGNORECASE)
    # express js regex rules for catching tainted variables with user input
    express_js_pattern = re.compile(r'(?:req|request)\.(?:body|params|query|headers|param|queryparam|get|post|paramfrom)', re.IGNORECASE)

    php_match = re.search(php_pattern, code_snippet)
    js_match = re.search(js_pattern, code_snippet)
    express_js_match = re.search(express_js_pattern, code_snippet)

    return bool(php_match), bool(js_match), bool(express_js_match)


def get_tainted_variables(references):
    tainted_variables = set()

    for var, snippets in references:
        for snippet in snippets:
            matches = check_variable_usage(snippet)
            if any(matches):
                tainted_variables.add(var)

    return list(tainted_variables)


def extract_tainted_snippets(references, tainted_variables):
    tainted_var_and_snippets = []

    regex_pattern = r'(?<![a-zA-Z0-9_]){}(?![a-zA-Z0-9_])'

    for tainted_var in tainted_variables:
        tainted_snippets = set()  # Initialize a set to store tainted snippets for each variable so that we don't have duplicates
        for var, snippets in references:
            for snippet in snippets:
                if re.findall(regex_pattern.format(re.escape(tainted_var)), snippet, flags=re.IGNORECASE):
                    tainted_snippets.add(snippet)  # Add the tainted snippet to the set
                    break  # Stop searching for this snippet if a tainted variable is found
        # Append variable and its tainted snippets
        tainted_var_and_snippets.append((tainted_var, list(tainted_snippets)))  # Convert the set to a list and append to the list of tainted variables and snippets

    return tainted_var_and_snippets


def sqli_vulnerability(data):
    sql_syntax_pattern = re.compile(r'\b(?:SELECT|INSERT|UPDATE|DELETE|FROM|WHERE|AND|OR)\b', re.IGNORECASE)
    concatenated_string_pattern = re.compile(r'["\']\s*\.\s*["\']')

    # Initialize counters for SQL injection patterns
    sql_syntax_count = 0
    concatenated_string_count = 0

    # Combine snippets from all categories into a single list
    all_snippets = [snippet for _, snippets in data for snippet in snippets]

    # Iterate over each snippet and detect SQLi vulnerabilities
    for snippet in all_snippets:
        if re.search(sql_syntax_pattern, snippet):
            sql_syntax_count += 1
        if re.search(concatenated_string_pattern, snippet):
            concatenated_string_count += 1

    if sql_syntax_count > 0:
        sql_syntax_count = 1
    if concatenated_string_count > 0:
        concatenated_string_count = 1

    # Return a single list containing the count of patterns found
    return [sql_syntax_count, concatenated_string_count]


def xss_vulnerability(data):
    html_tag_pattern = re.compile(r'<(?:'
        # Opening HTML tags for common XSS-vulnerable elements
        r'script|img|iframe|frame|a|form|input|textarea|svg'
        # Additional attributes for some tags
        r'(?:\s+[a-z0-9_-]+(?:\s*=\s*(?:"[^"]*"|\'[^\']*\'|[^>\s]+))?)*\s*/?'
        # Closing HTML tags for script, iframe, frame, a, form, textarea
        r'|\/(?:script|iframe|frame|a|form|textarea)'
        r')>'
    )
    concatenated_string_pattern = re.compile(r'["\']\s*\.\s*["\']')

    html_tag_count = 0
    concatenated_string_count = 0

    # Combine snippets from all categories into a single list
    all_snippets = [snippet for _, snippets in data for snippet in snippets]

    # Iterate over each snippet and detect XSS vulnerabilities
    for snippet in all_snippets:
        if re.search(html_tag_pattern, snippet):
            html_tag_count += 1
        if re.search(concatenated_string_pattern, snippet):
            concatenated_string_count += 1

    if html_tag_count > 0:
        html_tag_count = 1
    if concatenated_string_count > 0:
        concatenated_string_count = 1

    return [html_tag_count, concatenated_string_count]  # Adjust to fit the expected output format


def command_injection(data):
    system_call_pattern = re.compile(r'\b(?:exec|system|shell_exec|passthru)\b', re.IGNORECASE)
    invoked_function_pattern = re.compile(r'\b(?:eval|create_function)\b', re.IGNORECASE)
    concatenated_string_pattern = re.compile(r'["\']\s*\.\s*["\']')

    system_call_count = 0
    invoked_function_count = 0
    concatenated_string_count = 0

    # Combine snippets from all categories into a single list
    all_snippets = [snippet for _, snippets in data for snippet in snippets]

    # Iterate over each snippet and detect command injection vulnerabilities
    for snippet in all_snippets:
        if re.search(system_call_pattern, snippet):
            system_call_count += 1
        if re.search(invoked_function_pattern, snippet):
            invoked_function_count += 1
        if re.search(concatenated_string_pattern, snippet):
            concatenated_string_count += 1

    if system_call_count > 0:
        system_call_count = 1
    if invoked_function_count > 0:
        invoked_function_count = 1
    if concatenated_string_count > 0:
        concatenated_string_count = 1

    return [system_call_count, invoked_function_count, concatenated_string_count]


def prototype_pollution(data):
    prototype_assignment_pattern = re.compile(r'Object\.prototype\.[\w$]+\s*=\s*.+')
    object_assignment_pattern = re.compile(r'([\w$]+|Object)\s*=\s*{[\w$]+:\s*.+,')
    object_manipulation_pattern = re.compile(r'Object\.(assign|setPrototypeOf)\s*\([\w$]+\s*,\s*{[\w$]+:\s*.+}\s*\)')
    json_parse_pattern = re.compile(r'JSON\.parse\s*\([\w$]+\s*\)')
    property_check_pattern = re.compile(r'\bif\s*\(\s*!\s*[\w$]+\s*\.hasOwnProperty\s*\(\s*[\w$]+\s*\)\s*\)\s*{')
    default_object_assignment_pattern = re.compile(r'[\w$]+\s*=\s*[\w$]+\s*\|\|\s*{};')
    dynamic_property_assignment_pattern = re.compile(r'[\w$]+\s*\[\s*[\w$]+\s*\]\s*=\s*.+')
    array_copy_pattern = re.compile(r'const\s+[\w$]+\s*=\s*[\w$]+\s*\[\s*[\w$]+\s*\];')

    prototype_assignment_count = 0
    object_assignment_count = 0
    object_manipulation_count = 0
    json_parse_count = 0
    property_check_count = 0
    default_object_assignment_count = 0
    dynamic_property_assignment_count = 0
    array_copy_count = 0

    all_snippets = [snippet for _, snippets in data for snippet in snippets]

    for snippet in all_snippets:
        if re.search(prototype_assignment_pattern, snippet):
            prototype_assignment_count += 1
        if re.search(object_assignment_pattern, snippet):
            object_assignment_count += 1
        if re.search(object_manipulation_pattern, snippet):
            object_manipulation_count += 1
        if re.search(json_parse_pattern, snippet):
            json_parse_count += 1
        if re.search(property_check_pattern, snippet):
            property_check_count += 1
        if re.search(default_object_assignment_pattern, snippet):
            default_object_assignment_count += 1
        if re.search(dynamic_property_assignment_pattern, snippet):
            dynamic_property_assignment_count += 1
        if re.search(array_copy_pattern, snippet):
            array_copy_count += 1

    return [prototype_assignment_count, object_assignment_count, object_manipulation_count,
            json_parse_count, property_check_count, default_object_assignment_count,
            dynamic_property_assignment_count, array_copy_count]

def file_inclusion(data):
    php_dynamic_inclusion_pattern = re.compile(r'(include|require)(_once)?\s*\(.*?\$_(GET|POST|REQUEST|COOKIE)', re.IGNORECASE)
    php_unsanitized_inclusion_pattern = re.compile(r'(include|require)(_once)?\s*\(.*?\$_(GET|POST|REQUEST|COOKIE)', re.IGNORECASE)
    php_allow_url_include_pattern = re.compile(r'allow_url_include\s*=\s*(1|On)', re.IGNORECASE)
    php_dynamic_path_pattern = re.compile(r'(include|require)(_once)?\s*\(.*?".*?\$_(GET|POST|REQUEST|COOKIE).*?\.\w+', re.IGNORECASE)
    php_directory_traversal_pattern = re.compile(r'(include|require)(_once)?\s*\(.*?\.+\.\.\/', re.IGNORECASE)
    php_sensitive_file_access_pattern = re.compile(r'(include|require)(_once)?\s*\(.*?(config|passwords|settings)\.php', re.IGNORECASE)

    js_dynamic_inclusion_pattern = re.compile(r'(import|require)\s*\(\s*.*?["\']\s*\+\s*(?:\$GET|\$POST|\$REQUEST|\$COOKIE)', re.IGNORECASE)
    js_unsanitized_inclusion_pattern = re.compile(r'(import|require)\s*\(\s*.*?["\']\s*\+\s*(?:\$GET|\$POST|\$REQUEST|\$COOKIE)', re.IGNORECASE)

    dynamic_inclusion_count = 0
    unsanitized_inclusion_count = 0
    php_allow_url_include_count = 0
    php_dynamic_path_count = 0
    php_directory_traversal_count = 0
    php_sensitive_file_access_count = 0

    all_snippets = [snippet for _, snippets in data for snippet in snippets]

    for snippet in all_snippets:
        dynamic_inclusion_count += len(re.findall(php_dynamic_inclusion_pattern, snippet)) + len(re.findall(js_dynamic_inclusion_pattern, snippet))
        unsanitized_inclusion_count += len(re.findall(php_unsanitized_inclusion_pattern, snippet)) + len(re.findall(js_unsanitized_inclusion_pattern, snippet))
        php_allow_url_include_count += len(re.findall(php_allow_url_include_pattern, snippet))
        php_dynamic_path_count += len(re.findall(php_dynamic_path_pattern, snippet))
        php_directory_traversal_count += len(re.findall(php_directory_traversal_pattern, snippet))
        php_sensitive_file_access_count += len(re.findall(php_sensitive_file_access_pattern, snippet))

    return [dynamic_inclusion_count, unsanitized_inclusion_count, php_allow_url_include_count,
            php_dynamic_path_count, php_directory_traversal_count, php_sensitive_file_access_count]


def authentication_bypass(data):
    weak_authentication_pattern = re.compile(r'(login|authenticate)\s*\(.*?\btrue\b', re.IGNORECASE)
    hardcoded_credentials_pattern = re.compile(r'(login|authenticate)\s*\(.*?[\'"].*?[\'"]\s*,\s*[\'"].*?[\'"]\s*\)', re.IGNORECASE)
    bypass_logic_pattern = re.compile(r'(if|else\s*if)\s*\(.*?authenticated\s*[=!]=\s*true', re.IGNORECASE)
    commented_out_authentication_pattern = re.compile(r'/\*.*?(login|authenticate).*?\btrue\b.*?\*/', re.IGNORECASE)

    # Initialize counters for authentication bypass patterns
    weak_authentication_count = 0
    hardcoded_credentials_count = 0
    bypass_logic_count = 0
    commented_out_authentication_count = 0

    # Combine snippets from all categories into a single list
    all_snippets = [snippet for _, snippets in data for snippet in snippets]

    # Iterate over each snippet and detect authentication bypass vulnerabilities
    for snippet in all_snippets:
        if re.search(weak_authentication_pattern, snippet):
            weak_authentication_count += 1
        if re.search(hardcoded_credentials_pattern, snippet):
            hardcoded_credentials_count += 1
        if re.search(bypass_logic_pattern, snippet):
            bypass_logic_count += 1
        if re.search(commented_out_authentication_pattern, snippet):
            commented_out_authentication_count += 1

    # Convert counts to 1 if vulnerabilities are detected, else keep them as 0
    weak_authentication_count = 1 if weak_authentication_count > 0 else 0
    hardcoded_credentials_count = 1 if hardcoded_credentials_count > 0 else 0
    bypass_logic_count = 1 if bypass_logic_count > 0 else 0
    commented_out_authentication_count = 1 if commented_out_authentication_count > 0 else 0

    # Return a single list containing the counts of patterns found
    return [weak_authentication_count, hardcoded_credentials_count, bypass_logic_count, commented_out_authentication_count]

def excessive_data(data):
    verbose_error_messages_pattern = re.compile(r'(error|exception|warning):\s*(.)', re.IGNORECASE)
    debugging_info_pattern = re.compile(r'(debug|trace):\s(.)', re.IGNORECASE)
    excessive_logging_pattern = re.compile(r'(log|write_to_file):\s(.)', re.IGNORECASE)
    excessive_response_data_pattern = re.compile(r'(response|output):\s(.)', re.IGNORECASE)
    insecure_data_storage_pattern = re.compile(r'(store|save)_data(.∗)(.∗)', re.IGNORECASE)
    insecure_transmission_pattern = re.compile(r'(http|ftp)://', re.IGNORECASE)
    client_side_data_exposure_pattern = re.compile(r'(api_key|auth_token):\s(.)', re.IGNORECASE)
    pii_disclosure_pattern = re.compile(r'(name|address|social_security|medical_record):\s(.)', re.IGNORECASE)
    system_config_disclosure_pattern = re.compile(r'(system_config|software_version|infrastructure):\s(.)', re.IGNORECASE)
    misconfigured_access_controls_pattern = re.compile(r'(access_control|authorization):\s(.*)', re.IGNORECASE)

    # Initialize counters for excessive data patterns
    verbose_error_messages_count = 0
    debugging_info_count = 0
    excessive_logging_count = 0
    excessive_response_data_count = 0
    insecure_data_storage_count = 0
    insecure_transmission_count = 0
    client_side_data_exposure_count = 0
    pii_disclosure_count = 0
    system_config_disclosure_count = 0
    misconfigured_access_controls_count = 0

    # Combine snippets from all categories into a single list
    all_snippets = [snippet for _, snippets in data for snippet in snippets]

    # Iterate over each snippet and detect excessive data vulnerabilities
    for snippet in all_snippets:
        if re.search(verbose_error_messages_pattern, snippet):
            verbose_error_messages_count += 1
        if re.search(debugging_info_pattern, snippet):
            debugging_info_count += 1
        if re.search(excessive_logging_pattern, snippet):
            excessive_logging_count += 1
        if re.search(excessive_response_data_pattern, snippet):
            excessive_response_data_count += 1
        if re.search(insecure_data_storage_pattern, snippet):
            insecure_data_storage_count += 1
        if re.search(insecure_transmission_pattern, snippet):
            insecure_transmission_count += 1
        if re.search(client_side_data_exposure_pattern, snippet):
            client_side_data_exposure_count += 1
        if re.search(pii_disclosure_pattern, snippet):
            pii_disclosure_count += 1
        if re.search(system_config_disclosure_pattern, snippet):
            system_config_disclosure_count += 1
        if re.search(misconfigured_access_controls_pattern, snippet):
            misconfigured_access_controls_count += 1

    # Convert counts to 1 if vulnerabilities are detected, else keep them as 0
    verbose_error_messages_count = 1 if verbose_error_messages_count > 0 else 0
    debugging_info_count = 1 if debugging_info_count > 0 else 0
    excessive_logging_count = 1 if excessive_logging_count > 0 else 0
    excessive_response_data_count = 1 if excessive_response_data_count > 0 else 0
    insecure_data_storage_count = 1 if insecure_data_storage_count > 0 else 0
    insecure_transmission_count = 1 if insecure_transmission_count > 0 else 0
    client_side_data_exposure_count = 1 if client_side_data_exposure_count > 0 else 0
    pii_disclosure_count = 1 if pii_disclosure_count > 0 else 0
    system_config_disclosure_count = 1 if system_config_disclosure_count > 0 else 0
    misconfigured_access_controls_count = 1 if misconfigured_access_controls_count > 0 else 0

    # Return a single list containing the counts of patterns found
    return [verbose_error_messages_count, debugging_info_count, excessive_logging_count,
            excessive_response_data_count, insecure_data_storage_count, insecure_transmission_count,
            client_side_data_exposure_count, pii_disclosure_count, system_config_disclosure_count,
            misconfigured_access_controls_count]


def compute_combined_matrix(matrix):
    combined_matrix = [1 if any(row) else 0 for row in matrix]
    return combined_matrix


def preprocess(file_loc, lang):
    # Extract the variables from the code
    vars = execute_getvars(file_loc, lang)
    # Clean the code
    code = code_cleaner(file_loc)
    # Extract the variable references
    references = extract_vars_references(vars, code)
    # Get the tainted variables
    tainted_variables = get_tainted_variables(references)
    # Extract the tainted snippets
    tainted_snippets = extract_tainted_snippets(references, tainted_variables)
    # Extract the map
    all_snippets = [(var, snippets) for var, snippets in tainted_snippets]

    sqli_flags = sqli_vulnerability(all_snippets)
    xss_flags = xss_vulnerability(all_snippets)
    cmd_injection_flags = command_injection(all_snippets)
    prototype_pollution_flags = prototype_pollution(all_snippets)
    file_inclusion_flags = file_inclusion(all_snippets)
    authentication_bypass_flags = authentication_bypass(all_snippets)
    excessive_data_flags = excessive_data(all_snippets)


    matrix = [
            list(sqli_flags),
            list(xss_flags),
            list(cmd_injection_flags),
            list(prototype_pollution_flags),
            list(file_inclusion_flags),
            list(authentication_bypass_flags),
            list(excessive_data_flags)
        ]
    
    max_length = max(len(row) for row in matrix)
    for row in matrix:
        while len(row) < max_length:
            row.append(0)

    # Don't print when extracting to make this faster

    # print("\nX-Feature:")
    # for row in matrix:
    #     print(row)

    # print("\nY-Feature:")
    # combined_matrix = compute_combined_matrix(matrix)
    # print(combined_matrix)

    # Todo: Save the combined matrix as I have instructed in the Teams 
    # Write the result to a CSV file


def main():
    php_samples = [os.path.join(php_samples_loc, f) for f in os.listdir(php_samples_loc) if os.path.isfile(os.path.join(php_samples_loc, f))]
    js_samples = [os.path.join(js_samples_loc, f) for f in os.listdir(js_samples_loc) if os.path.isfile(os.path.join(js_samples_loc, f))]

    for file in php_samples:
        print(f"\nProcessing {file}...")
        preprocess(file, "php")

    for file in js_samples:
        print(f"\nProcessing {file}...")
        preprocess(file, "js")


if __name__ == "__main__":
    main()