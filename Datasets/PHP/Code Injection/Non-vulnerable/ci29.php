<?php 
// Remediation
$cmd = getenv('CMD');
$cmd = escapeshellcmd($cmd);
exec($cmd);

?> 
