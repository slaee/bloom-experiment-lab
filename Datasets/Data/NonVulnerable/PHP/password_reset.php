<?php
  $token = bin2hex(random_bytes(32));
  $reset_link = "https://example.com/reset_password?token=$token";
  echo "Password reset link: $reset_link";
?>

