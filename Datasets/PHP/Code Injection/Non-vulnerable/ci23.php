<?php 
// Remediation
$cmd = getenv('CMD');
$cmd = escapeshellcmd($cmd);
system($cmd);

?> 
