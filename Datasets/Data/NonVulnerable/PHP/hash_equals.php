<?php
  $hash1 = password_hash('password123', PASSWORD_DEFAULT);
  $hash2 = password_hash('password123', PASSWORD_DEFAULT);

  if (hash_equals($hash1, $hash2)) {
    echo "Passwords match.";
  } else {
    echo "Passwords do not match.";
  }
?>
