<?php 
// Remediation
$cmd = $_GET['cmd'];
$cmd = htmlspecialchars($cmd); // Sanitize input
eval($cmd);

?> 
