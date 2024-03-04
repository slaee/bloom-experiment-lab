<?php 
// Vulnerable code
$filename = getenv('FILENAME');
$file_content = getenv('FILE_CONTENT');
file_put_contents($filename, $file_content);

?> 
