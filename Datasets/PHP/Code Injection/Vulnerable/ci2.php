<?php 
// Vulnerable code
$filename = $_POST['filename'];
$content = $_POST['content'];
file_put_contents($filename, $content);

?> 
