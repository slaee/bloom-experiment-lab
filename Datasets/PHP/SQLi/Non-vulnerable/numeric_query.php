<?php
$price = $_POST['price'];
$query = "SELECT * FROM products WHERE price=?";
$stmt = mysqli_prepare($connection, $query);
mysqli_stmt_bind_param($stmt, "d", $price);
mysqli_stmt_execute($stmt);
$result = mysqli_stmt_get_result($stmt);

?>