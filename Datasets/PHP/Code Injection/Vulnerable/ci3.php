<?php 
// Vulnerable code
$cmd = $_REQUEST['cmd'];
exec($cmd);

?> 
