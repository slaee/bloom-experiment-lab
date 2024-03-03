<?php
  $stmt = $pdo->prepare("INSERT INTO users (name, email) VALUES (?, ?)");
  $stmt->execute(['John Doe', 'john@example.com']);
  echo "User added successfully.";
?>
