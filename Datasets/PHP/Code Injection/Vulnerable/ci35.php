<?php 
// Vulnerable code
$referrer = $_SERVER['HTTP_REFERER'];
echo "Referrer: $referrer";

?> 
