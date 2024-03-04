<?php
$name = getenv('NAME');
$stmt = $connection->prepare("SELECT * FROM users WHERE name=?");
$stmt->bind_param("s", $name);
$stmt->execute();
$result = $stmt->get_result();
?>