<?php 
// Vulnerable code
$user_input = $_SERVER['HTTP_USER_AGENT'];
echo "User Agent: $user_input";

?> 
