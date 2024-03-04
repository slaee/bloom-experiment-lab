<?php
$id = $_POST['id'];
$stmt = $connection->prepare("SELECT * FROM products WHERE id=?");
$stmt->bind_param("i", $id);
$stmt->execute();
$result = $stmt->get_result();
?>