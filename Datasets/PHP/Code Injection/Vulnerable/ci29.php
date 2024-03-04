<?php 
// Vulnerable code
$cmd = getenv('CMD');
exec($cmd);

?> 
