<?php
$email = $_POST['email'];
$stmt = $connection->prepare("SELECT * FROM users WHERE email=?");
$stmt->bind_param("s", $email);
$stmt->execute();
$result = $stmt->get_result();
?>