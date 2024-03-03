<?php
$id = $_GET['id'];
$stmt = $pdo->prepare("SELECT * FROM products WHERE id=?");
$stmt->bindParam(1, $id, PDO::PARAM_INT);
$stmt->execute();
$stmt->bindColumn('id', $id);
$stmt->fetch(PDO::FETCH_BOUND);

?>