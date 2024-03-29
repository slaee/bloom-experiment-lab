import re


sql_string = """
$array = array();
$array[] = 'safe' ;
$array[] = $_GET['userData'] ;
$array[] = 'safe' ;
$tainted = $array[1] ;

$legal_table = array("safe1", "safe2");
if (in_array($tainted, $legal_table, true)) {
  $tainted = $tainted;
} else {
  $tainted = $legal_table[0];
}

//flaw
echo "Test". $test;
"""

"""
Pattern for concatenation:
    case 1 and case 2
    optionalGroup( ( " or ' or ` ) \s* ( + or . ) \s*) anychar_except( " or ' or ` ) optionalGroup( \s* ( + or . ) \s* ( " or ' or ` ) )

    case 3 
    let strings = requiredGroup ( " or ` ) anychar requiredGroup ( " or ` )
    - strings contains $anychar or ${anychar}
    - consider a string like "SELECT * FROM users WHERE user_id = '$userid1_2'"
    - consider a string like `SELECT * FROM users WHERE user_id = ${userid1_2}`
"""
def hasConcatenation(statement):
    case1 = re.compile(r'(["\'`]\s*[+\.]\s*?)\(?[a-zA-Z0-9_$]\)?[^"\'`]')
    case2 = re.compile(r'[^"\'`]\(?[a-zA-Z0-9_$]\)?\s*[+\.]\s*?["\'`]')
    case3 = re.compile(r'(\$\w+)|(\$\{\w+\})')
    grab_string = re.compile(r'(["`]).*?\1')
    string = re.finditer(grab_string, statement)
    # check for case 1 and case 2
    if re.search(case1, statement) or re.search(case2, statement):
        return True
    # if no match found in case 1 and case 2, check for case 3
    for s in string:
        if re.search(case3, s.group()):
            return True
    # if not match found in case 1-3, return False
    return False

def matchHTMLTags(statement):
    # Define a pattern to match HTML tags
    html_tag_pattern = re.compile(r'<.*?>')
    # detect echo $anyvar
    echo_pattern = re.compile(r'echo\s*\$')
    # detect echo function 
    echo_function_pattern = re.compile(r'\b(?:echo|print|printf|sprintf|vprintf|vsprintf|innertext|outerhtml|innerHTML|outerHTML|document.write|document.writeln|document.open|document.close|document.writeIn|document.writeLn|document.writeInLn|text\s*=)\b', re.IGNORECASE)


    # Initialize counts to zero
    html_tag_count = 0
    concatenated_string_count = 0
    if re.search(html_tag_pattern, statement) or re.search(echo_function_pattern, statement):
        html_tag_count = 1
        if hasConcatenation(statement):
            concatenated_string_count = 1
    if re.search(echo_pattern, statement):
        html_tag_count = 1
        concatenated_string_count = 1
    # Return a single list containing the count of patterns found
    return [html_tag_count, concatenated_string_count]

# This will match SQL syntax and concatenated strings in a given SQL statement.
def matchSqlStament(statement):
    # Define a pattern to match SQL syntax
    sql_syntax_pattern = re.compile(r'\b(?:SELECT|INSERT|UPDATE|DELETE|FROM|WHERE|AND|OR)\b', re.IGNORECASE)
    # Initialize counts to zero
    sql_syntax_count = 0
    concatenated_string_count = 0
    if re.search(sql_syntax_pattern, statement):
        sql_syntax_count = 1
        if hasConcatenation(statement):
            concatenated_string_count = 1
    # Return a single list containing the count of patterns found
    return [sql_syntax_count, concatenated_string_count]

def matchDangerousFunctions(statement):
    # Define a pattern to match dangerous functions
    dangerous_function_pattern = re.compile(r'\b(?:exec|system|shell_exec|passthru|eval|create_function|popen|proc_open|preg_replace|unserialize|Function|setTimeout|setInterval|spawn|execSync|execFile)\b', re.IGNORECASE)
    # Initialize counts to zero
    dangerous_function_count = 0
    concatenated_string_count = 0
    if re.search(dangerous_function_pattern, statement):
        dangerous_function_count = 1
        if hasConcatenation(statement):
            concatenated_string_count = 1
    # Return a single list containing the count of patterns found
    return [dangerous_function_count, concatenated_string_count]


def matchValidationFunctions(statement):
    # Define a pattern to match validation functions
    validation_function_pattern = re.compile(r'\b(?:isset|filter_var|filter_input|filter_var_array|filter_input_array|preg_match|preg_match_all|preg_replace|preg_replace_callback|preg_replace_callback_array|preg_split|preg_grep|preg_filter|preg_last_error|is_numeric|is_int|is_float|is_string|ctype_digit|ctype_alpha|test|match|validate|check|verify|sanitize|clean|escape|encode|decode|hash|encrypt|decrypt|secure|validate|check|verify|sanitize|clean|escape|encode|decode|hash|encrypt|decrypt|secure)\b', re.IGNORECASE)
    operator_check_pattern = re.compile(r'\b(?:==|===|!=|!==|<=|>=|<|>)\b')
    if_statement_pattern = re.compile(r'\bif\s*\(\s*.*\s*\)')
    # Initialize counts to zero
    validation_function_count = 0
    operator_check_count = 0
    if_statement_count = 0
    if re.search(if_statement_pattern, statement):
        if_statement_count = 1
    if re.search(validation_function_pattern, statement):
        validation_function_count = 1
    if re.search(operator_check_pattern, statement):
        operator_check_count = 1
    return [if_statement_count, validation_function_count, operator_check_count]

print(matchHTMLTags(sql_string))
