<?php 
// Remediation
$referrer = $_SERVER['HTTP_REFERER'];
$referrer = htmlspecialchars($referrer);
echo "Referrer: $referrer";

?> 
