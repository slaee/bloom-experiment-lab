<?php
$id = $_SERVER['QUERY_STRING'];
$query = "SELECT * FROM products WHERE id='$id'";
$result = mysqli_query($connection, $query);
?>