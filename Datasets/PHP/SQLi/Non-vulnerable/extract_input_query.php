<?php
extract($_GET);
$stmt = $pdo->prepare("SELECT * FROM products WHERE category=:category");
$stmt->execute(['category' => $category]);
$result = $stmt->fetchAll();
?>