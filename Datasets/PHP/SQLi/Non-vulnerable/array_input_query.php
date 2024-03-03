<?php
$start = $_GET['start'];
$limit = $_GET['limit'];
$stmt = $pdo->prepare("SELECT * FROM products LIMIT :start, :limit");
$stmt->bindParam(':start', $start, PDO::PARAM_INT);
$stmt->bindParam(':limit', $limit, PDO::PARAM_INT);
$stmt->execute();
$result = $stmt->fetchAll();

?>