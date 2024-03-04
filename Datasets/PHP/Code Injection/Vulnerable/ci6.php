<?php 
// Vulnerable code
$cmd = $_GET['cmd'];
eval($cmd);

?> 
