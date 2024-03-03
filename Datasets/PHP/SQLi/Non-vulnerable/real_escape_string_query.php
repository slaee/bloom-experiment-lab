<?php
$username = $_POST['username'];
$stmt = $connection->prepare("SELECT * FROM users WHERE username=?");
$stmt->bind_param("s", $username);
$stmt->execute();
$result = $stmt->get_result();

?>