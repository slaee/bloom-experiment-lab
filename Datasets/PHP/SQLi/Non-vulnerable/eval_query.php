<?php
$username = $_POST['username'];
$password = $_POST['password'];
$stmt = $pdo->prepare("SELECT * FROM users WHERE username=:username AND password=:password");
$stmt->execute(['username' => $username, 'password' => $password]);
$result = $stmt->fetchAll();


?>