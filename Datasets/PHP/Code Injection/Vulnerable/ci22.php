<?php 
// Vulnerable code
$command = $_REQUEST['command'];
echo shell_exec($command);
?> 
