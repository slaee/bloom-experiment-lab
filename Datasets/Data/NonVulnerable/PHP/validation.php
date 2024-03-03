<?php
  $email = "user@example.com";

  if (filter_var($email, FILTER_VALIDATE_EMAIL)) {
    echo "Valid email address";
  } else {
    echo "Invalid email address";
  }
?>
