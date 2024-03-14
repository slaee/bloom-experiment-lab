import re
import sys

def detect_sqli_vulnerability(code):
    sql_syntax_pattern = re.compile(r'\b(?:SELECT|INSERT|UPDATE|DELETE|FROM|WHERE|AND|OR)\b', re.IGNORECASE)
    #sql_function_pattern = re.compile(r'\b(?:mysql_query|mysqli_query|pg_query|sqlite_query)\b', re.IGNORECASE)
    concatenated_string_pattern = re.compile(r'["\']\s*\.\s*["\']')

    sql_syntax_count = 1 if len(re.findall(sql_syntax_pattern, code)) > 0 else 0
    #sql_function_count = 1 if len(re.findall(sql_function_pattern, code)) > 0 else 0
    concatenated_string_count = 1 if len(re.findall(concatenated_string_pattern, code)) > 0 else 0

    return sql_syntax_count, concatenated_string_count

def detect_xss_vulnerability(code):
    # regex for html tags for both PHP and JS code vulnerable to XSS    
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

    html_tag_count = 1 if len(re.findall(html_tag_pattern, code)) > 0 else 0
    concatenated_string_count = 1 if len(re.findall(concatenated_string_pattern, code)) > 0 else 0

    return html_tag_count, 0, concatenated_string_count

def detect_command_injection(code):
    system_call_pattern = re.compile(r'\b(?:exec|system|shell_exec|passthru)\b', re.IGNORECASE)
    invoked_function_pattern = re.compile(r'\b(?:eval|create_function)\b', re.IGNORECASE)
    concatenated_string_pattern = re.compile(r'["\']\s*\.\s*["\']')

    system_call_count = 1 if len(re.findall(system_call_pattern, code)) > 0 else 0
    invoked_function_count = 1 if len(re.findall(invoked_function_pattern, code)) > 0 else 0
    concatenated_string_count = 1 if len(re.findall(concatenated_string_pattern, code)) > 0 else 0

    return system_call_count, invoked_function_count, concatenated_string_count

def detect_prototype_pollution(code):
    prototype_assignment_pattern = re.compile(r'Object\.prototype\.[\w$]+\s*=\s*.+')
    object_assignment_pattern = re.compile(r'([\w$]+|Object)\s*=\s*{[\w$]+:\s*.+,')
    object_manipulation_pattern = re.compile(r'Object\.(assign|setPrototypeOf)\s*\([\w$]+\s*,\s*{[\w$]+:\s*.+}\s*\)')
    json_parse_pattern = re.compile(r'JSON\.parse\s*\([\w$]+\s*\)')
    property_check_pattern = re.compile(r'\bif\s*\(\s*!\s*[\w$]+\s*\.hasOwnProperty\s*\(\s*[\w$]+\s*\)\s*\)\s*{')
    default_object_assignment_pattern = re.compile(r'[\w$]+\s*=\s*[\w$]+\s*\|\|\s*{};')
    dynamic_property_assignment_pattern = re.compile(r'[\w$]+\s*\[\s*[\w$]+\s*\]\s*=\s*.+')
    array_copy_pattern = re.compile(r'const\s+[\w$]+\s*=\s*[\w$]+\s*\[\s*[\w$]+\s*\];')

    prototype_assignment_count = 1 if len(re.findall(prototype_assignment_pattern, code)) > 0 else 0   
    object_assignment_count = 1 if len(re.findall(object_assignment_pattern, code)) > 0 else 0
    object_manipulation_count = 1 if len(re.findall(object_manipulation_pattern, code)) > 0 else 0
    json_parse_count = 1 if len(re.findall(json_parse_pattern, code)) > 0 else 0
    property_check_count = 1 if len(re.findall(property_check_pattern, code)) > 0 else 0
    default_object_assignment_count = 1 if len(re.findall(default_object_assignment_pattern, code)) > 0 else 0
    dynamic_property_assignment_count = 1 if len(re.findall(dynamic_property_assignment_pattern, code)) > 0 else 0
    array_copy_count = 1 if len(re.findall(array_copy_pattern, code)) > 0 else 0

    return (prototype_assignment_count, object_assignment_count, object_manipulation_count,
            json_parse_count, property_check_count, default_object_assignment_count,
            dynamic_property_assignment_count, array_copy_count)

def detect_file_inclusion(code):
    # Patterns for detecting File Inclusion vulnerabilities in PHP code
    php_dynamic_inclusion_pattern = re.compile(r'(include|require)(_once)?\s*\(.*?\$_(GET|POST|REQUEST|COOKIE)', re.IGNORECASE)
    php_unsanitized_inclusion_pattern = re.compile(r'(include|require)(_once)?\s*\(.*?\$_(GET|POST|REQUEST|COOKIE)', re.IGNORECASE)
    php_allow_url_include_pattern = re.compile(r'allow_url_include\s*=\s*(1|On)', re.IGNORECASE)
    php_dynamic_path_pattern = re.compile(r'(include|require)(_once)?\s*\(.*?".*?\$_(GET|POST|REQUEST|COOKIE).*?\.\w+', re.IGNORECASE)
    php_directory_traversal_pattern = re.compile(r'(include|require)(_once)?\s*\(.*?\.+\.\.\/', re.IGNORECASE)
    php_sensitive_file_access_pattern = re.compile(r'(include|require)(_once)?\s*\(.*?(config|passwords|settings)\.php', re.IGNORECASE)

    # Patterns for detecting File Inclusion vulnerabilities in JavaScript code
    js_dynamic_inclusion_pattern = re.compile(r'(import|require)\s*\(\s*.*?["\']\s*\+\s*(?:\$GET|\$POST|\$REQUEST|\$COOKIE)', re.IGNORECASE)
    js_unsanitized_inclusion_pattern = re.compile(r'(import|require)\s*\(\s*.*?["\']\s*\+\s*(?:\$GET|\$POST|\$REQUEST|\$COOKIE)', re.IGNORECASE)

    dynamic_inclusion_count = 1 if (len(re.findall(php_dynamic_inclusion_pattern, code)) + len(re.findall(js_dynamic_inclusion_pattern, code))) > 0 else 0
    unsanitized_inclusion_count = 1 if (len(re.findall(php_unsanitized_inclusion_pattern, code)) + len(re.findall(js_unsanitized_inclusion_pattern, code))) > 0 else 0
    php_allow_url_include_count = 1 if len(re.findall(php_allow_url_include_pattern, code)) > 0 else 0
    php_dynamic_path_count = 1 if len(re.findall(php_dynamic_path_pattern, code)) > 0 else 0
    php_directory_traversal_count = 1 if len(re.findall(php_directory_traversal_pattern, code)) > 0 else 0
    php_sensitive_file_access_count = 1 if len(re.findall(php_sensitive_file_access_pattern, code)) > 0 else 0

    return (dynamic_inclusion_count, unsanitized_inclusion_count, php_allow_url_include_count,
            php_dynamic_path_count, php_directory_traversal_count, php_sensitive_file_access_count)

def detect_authentication_bypass(code):
    weak_authentication_pattern = re.compile(r'(login|authenticate)\s*\(.*?\btrue\b', re.IGNORECASE)
    hardcoded_credentials_pattern = re.compile(r'(login|authenticate)\s*\(.*?[\'"].*?[\'"]\s*,\s*[\'"].*?[\'"]\s*\)', re.IGNORECASE)
    bypass_logic_pattern = re.compile(r'(if|else\s*if)\s*\(.*?authenticated\s*[=!]=\s*true', re.IGNORECASE)
    commented_out_authentication_pattern = re.compile(r'/\*.*?(login|authenticate).*?\btrue\b.*?\*/', re.IGNORECASE)

    # Search for matches in the code
    weak_authentication_count = 1 if len(re.findall(weak_authentication_pattern, code)) > 0 else 0
    hardcoded_credentials_count = 1 if len(re.findall(hardcoded_credentials_pattern, code)) > 0 else 0
    bypass_logic_count = 1 if len(re.findall(bypass_logic_pattern, code)) > 0 else 0
    commented_out_authentication_count = 1 if len(re.findall(commented_out_authentication_pattern, code)) > 0 else 0

    return (weak_authentication_count, hardcoded_credentials_count, bypass_logic_count, commented_out_authentication_count)

def detect_excessive_data(code):
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

    verbose_error_messages_count = 1 if len(re.findall(verbose_error_messages_pattern, code)) > 0 else 0
    debugging_info_count = 1 if len(re.findall(debugging_info_pattern, code)) > 0 else 0
    excessive_logging_count = 1 if len(re.findall(excessive_logging_pattern, code)) > 0 else 0
    excessive_response_data_count = 1 if len(re.findall(excessive_response_data_pattern, code)) > 0 else 0
    insecure_data_storage_count = 1 if len(re.findall(insecure_data_storage_pattern, code)) > 0 else 0
    insecure_transmission_count = 1 if len(re.findall(insecure_transmission_pattern, code)) > 0 else 0
    client_side_data_exposure_count = 1 if len(re.findall(client_side_data_exposure_pattern, code)) > 0 else 0
    pii_disclosure_count = 1 if len(re.findall(pii_disclosure_pattern, code)) > 0 else 0
    system_config_disclosure_count = 1 if len(re.findall(system_config_disclosure_pattern, code)) > 0 else 0
    misconfigured_access_controls_count = 1 if len(re.findall(misconfigured_access_controls_pattern, code)) > 0 else 0

    return (verbose_error_messages_count, debugging_info_count, excessive_logging_count,
            excessive_response_data_count, insecure_data_storage_count, insecure_transmission_count,
            client_side_data_exposure_count, pii_disclosure_count, system_config_disclosure_count,
            misconfigured_access_controls_count)

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

        sql_counts = detect_sqli_vulnerability(code)
        xss_counts = detect_xss_vulnerability(code)
        command_counts = detect_command_injection(code)
        prototype_pollution_counts = detect_prototype_pollution(code)
        file_inclusion_counts = detect_file_inclusion(code)
        authentication_bypass_counts = detect_authentication_bypass(code)
        excessive_data_counts = detect_excessive_data(code)

        matrix = [
            list(sql_counts),
            list(xss_counts),
            list(command_counts),
            list(prototype_pollution_counts),
            list(file_inclusion_counts),
            list(authentication_bypass_counts),
            list(excessive_data_counts)
        ]

        max_length = max(len(row) for row in matrix)
        for row in matrix:
            while len(row) < max_length:
                row.append(0)

        vulnerability_labels = ["SQLi Vulnerability", "XSS Vulnerability", "Command Injection", "Prototype Pollution", "File Inclusion", "Authentication Bypass", "Excessive Data"]

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