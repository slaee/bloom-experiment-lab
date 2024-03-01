<?php
  $dsn = "mysql:host=localhost;dbname=my_database";
  $username = "root";
  $password = "";
  try {
    $pdo = new PDO($dsn, $username, $password);
    echo "Connected to the database.";
  } catch (PDOException $e) {
    die("Connection failed: " . $e->getMessage());
  }
?>
