<?php
$start = $_GET['start'];
$limit = $_GET['limit'];
$stmt = $pdo->prepare("SELECT * FROM products LIMIT :start, :limit");
$stmt->bindValue(':start', (int)$start, PDO::PARAM_INT);
$stmt->bindValue(':limit', (int)$limit, PDO::PARAM_INT);
$stmt->execute();
$result = $stmt->fetchAll();

?>