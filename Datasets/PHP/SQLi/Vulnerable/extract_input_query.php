<?php
extract($_GET);
$query = "SELECT * FROM products WHERE id=$id";
$result = mysqli_query($connection, $query);

?>