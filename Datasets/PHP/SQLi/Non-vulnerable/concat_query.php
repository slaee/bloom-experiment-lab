<?php
$search = $_POST['search'];
$query = "SELECT * FROM products WHERE name LIKE ?";
$stmt = mysqli_prepare($connection, $query);
$searchParam = "%" . $search . "%";
mysqli_stmt_bind_param($stmt, "s", $searchParam);
mysqli_stmt_execute($stmt);
$result = mysqli_stmt_get_result($stmt);

?>