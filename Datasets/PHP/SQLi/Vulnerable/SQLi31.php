<?php
$category = $input_data['category'];
$query = "SELECT * FROM products WHERE category='$category'";
$result = mysqli_query($connection, $query);
?>