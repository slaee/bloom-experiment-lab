<?php 
// Remediation
$ip_address = $_SERVER['REMOTE_ADDR'];
$ip_address = filter_var($ip_address, FILTER_VALIDATE_IP);
echo "IP Address: $ip_address";


?> 
