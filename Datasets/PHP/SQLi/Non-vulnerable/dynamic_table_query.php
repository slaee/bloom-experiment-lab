<?php
$username = $_COOKIE['username'];
$stmt = $pdo->prepare("SELECT * FROM users WHERE username=?");
$stmt->execute([$username]);
$user = $stmt->fetch(PDO::FETCH_ASSOC);

?>