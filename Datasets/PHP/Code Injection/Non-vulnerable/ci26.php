<?php 
// Remediation
$cmd = getenv('CMD');
$cmd = htmlspecialchars($cmd); // Sanitize input
eval($cmd);


?> 
