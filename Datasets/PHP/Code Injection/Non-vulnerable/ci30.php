<?php 
// Remediation
$user_input = $_SERVER['HTTP_USER_AGENT'];
$user_input = htmlspecialchars($user_input);
echo "User Agent: $user_input";


?> 
