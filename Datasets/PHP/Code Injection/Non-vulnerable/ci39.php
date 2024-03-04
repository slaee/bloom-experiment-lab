<?php 
// Remediation
$query = $_SERVER['QUERY_STRING'];
$query = filter_var($query, FILTER_SANITIZE_STRING);
echo "Query result: $query";

?> 
