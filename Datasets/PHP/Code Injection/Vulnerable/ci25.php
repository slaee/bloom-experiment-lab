<?php 
// Vulnerable code
$command = getenv('COMMAND');
echo shell_exec($command);

?> 
