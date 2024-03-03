<?php
$name = $_SERVER['HTTP_X_NAME'];
$stmt = $pdo->prepare("SELECT * FROM users WHERE name=:name");
$stmt->execute(['name' => $name]);
$result = $stmt->fetchAll();

?>