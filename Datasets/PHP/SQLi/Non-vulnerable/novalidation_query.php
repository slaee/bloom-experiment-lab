<?php
$username = $_POST['username'];
$password = $_POST['password'];
$stmt = $pdo->prepare("SELECT * FROM users WHERE username=? AND password=?");
$stmt->execute([$username, $password]);
$result = $stmt->fetchAll();

?>