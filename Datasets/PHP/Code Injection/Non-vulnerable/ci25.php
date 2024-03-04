<?php 
// Remediation
$command = getenv('COMMAND');
$command = escapeshellcmd($command);
echo shell_exec($command);


?> 
