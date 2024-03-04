<?php 
// Remediation
$filename = $_POST['filename'];
$file_content = $_POST['file_content'];
$filename = filter_var($filename, FILTER_SANITIZE_STRING); // Sanitize input
$file_content = filter_var($file_content, FILTER_SANITIZE_STRING); // Sanitize input
file_put_contents($filename, $file_content);

?> 
