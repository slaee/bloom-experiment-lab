<?php
$id = getenv('ID');
$stmt = $connection->prepare("SELECT * FROM products WHERE id=?");
$stmt->bind_param("s", $id);
$stmt->execute();
$result = $stmt->get_result();
?>