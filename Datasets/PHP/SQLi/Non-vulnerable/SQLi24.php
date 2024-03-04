<?php
$category = $request['category'];
$stmt = $connection->prepare("SELECT * FROM products WHERE category=?");
$stmt->bind_param("s", $category);
$stmt->execute();
$result = $stmt->get_result();
?>