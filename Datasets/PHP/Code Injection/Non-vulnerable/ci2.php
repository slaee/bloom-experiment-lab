<?php 
// Remediation
$filename = $_POST['filename'];
$content = $_POST['content'];
$filename = basename($filename); // Sanitize input
file_put_contents($filename, $content);

?> 
