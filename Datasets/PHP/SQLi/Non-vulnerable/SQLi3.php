<?php
$search = $_POST['search'];
$stmt = $connection->prepare("SELECT * FROM products WHERE name LIKE ?");
$searchParam = "%$search%";
$stmt->bind_param("s", $searchParam);
$stmt->execute();
$result = $stmt->get_result();
?>