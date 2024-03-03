<?php
$username = $_POST['username'];
$password = $_POST['password'];
$stmt = $connection->prepare("SELECT * FROM users WHERE username=? AND password=?");
$stmt->bind_param("ss", $username, $password);
$stmt->execute();
$result = $stmt->get_result();

?>