<?php
  $password = "SecurePwd123";

  if (strlen($password) >= 8 &&
      preg_match('/[A-Z]/', $password) &&
      preg_match('/[a-z]/', $password) &&
      preg_match('/[0-9]/', $password)) {
    echo "Password meets the required policy.";
  } else {
    echo "Password does not meet the required policy.";
  }
?>
