<?php
$id = $productId;
$query = "SELECT * FROM products WHERE id='$id'";
$result = mysqli_query($connection, $query);
?>