<?php 
// Vulnerable code
$cmd = getenv('CMD');
system($cmd);

?> 
