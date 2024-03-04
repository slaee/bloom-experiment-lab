<?php 
// Vulnerable code
$filename = getenv('FILENAME');
include($filename);

?> 
