<?php
$category = $request_data['category'];
$stmt = $connection->prepare("SELECT * FROM products WHERE category=?");
$stmt->bind_param("s", $category);
$stmt->execute();
$result = $stmt->get_result();
?>