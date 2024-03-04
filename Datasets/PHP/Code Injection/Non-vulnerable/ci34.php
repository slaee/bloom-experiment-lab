<?php 
// Remediation
$server_data = $_SERVER['SERVER_NAME'];
$server_data = htmlspecialchars($server_data);
echo "Server Name: $server_data";
?> 
