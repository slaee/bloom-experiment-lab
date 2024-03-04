<?php 
// Vulnerable code
$cmd = getenv('CMD');
eval($cmd);

?> 
