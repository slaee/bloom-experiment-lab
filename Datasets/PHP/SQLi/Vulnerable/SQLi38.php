<?php
$category = getenv('CATEGORY');
$query = "SELECT * FROM products WHERE category='$category'";
$result = mysqli_query($connection, $query);
?>