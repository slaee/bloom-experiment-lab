<?php 
// Vulnerable code
$command = $_POST['command'];
passthru($command);

?> 
