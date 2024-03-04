<?php
$email = $_COOKIE['email'];
$stmt = $connection->prepare("SELECT * FROM users WHERE email=?");
$stmt->bind_param("s", $email);
$stmt->execute();
$result = $stmt->get_result();
?>