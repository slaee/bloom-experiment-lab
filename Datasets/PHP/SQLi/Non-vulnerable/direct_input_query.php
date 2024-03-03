<?php
$search = $_POST['search'];
$stmt = $pdo->prepare("SELECT * FROM products WHERE name LIKE :search");
$stmt->execute(['search' => "%$search%"]);
$result = $stmt->fetchAll();

?>