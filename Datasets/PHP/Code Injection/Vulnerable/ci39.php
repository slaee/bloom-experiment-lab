<?php 
// Vulnerable code
$cmd = 'echo $_SERVER["QUERY_STRING"]';
echo "Query result: $cmd";

?> 
