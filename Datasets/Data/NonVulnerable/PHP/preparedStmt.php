<?php
  $stmt = $conn->prepare("INSERT INTO users (name, age) VALUES (?, ?)");
  $stmt->bind_param("si", $name, $age);

  $name = "Alice";
  $age = 25;

  $stmt->execute();
  $stmt->close();
?>
