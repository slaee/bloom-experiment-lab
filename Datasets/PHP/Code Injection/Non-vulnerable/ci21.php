<?php 
// Remediation
$filename = $_POST['filename'];
$filename = filter_var($filename, FILTER_SANITIZE_STRING); // Sanitize input
include($filename);
?> 
