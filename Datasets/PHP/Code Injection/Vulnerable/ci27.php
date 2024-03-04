<?php 
// Vulnerable code
$command = getenv('COMMAND');
passthru($command);

?> 
