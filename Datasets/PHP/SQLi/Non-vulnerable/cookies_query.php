<?php
$username = $_COOKIE['username'];
$stmt = $connection->prepare("SELECT * FROM users WHERE username=?");
$stmt->bind_param("s", $username);
$stmt->execute();
$stmt->bind_result($id, $username, $email);
$stmt->fetch();

?>