<?php
$id = getenv('ID');
$query = "SELECT * FROM products WHERE id='$id'";
$result = mysqli_query($connection, $query);
?>