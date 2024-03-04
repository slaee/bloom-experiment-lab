<?php
$name = $formData['name'];
$stmt = $connection->prepare("SELECT * FROM users WHERE name=?");
$stmt->bind_param("s", $name);
$stmt->execute();
$result = $stmt->get_result();
?>