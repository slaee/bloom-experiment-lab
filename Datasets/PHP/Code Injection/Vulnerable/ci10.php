<?php 
// Vulnerable code
$filename = $_POST['filename'];
$file_content = $_POST['file_content'];
file_put_contents($filename, $file_content);

?> 
