<?php 
// Vulnerable code
$filename = 'echo $_SERVER["PHP_SELF"]';
include($filename);
?> 
