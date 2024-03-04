<?php 
// Vulnerable code
$command = $_POST['command'];
echo shell_exec($command);

?> 
