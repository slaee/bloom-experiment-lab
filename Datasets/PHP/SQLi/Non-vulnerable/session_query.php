<?php       
$id = $_SESSION['id'];
$stmt = $pdo->prepare("SELECT * FROM users WHERE id=?");
$stmt->execute([$id]);
$result = $stmt->fetchAll();
?>