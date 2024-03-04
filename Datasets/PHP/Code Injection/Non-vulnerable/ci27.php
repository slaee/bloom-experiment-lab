<?php 
// Remediation
$command = getenv('COMMAND');
$command = escapeshellcmd($command);
passthru($command);
?> 
