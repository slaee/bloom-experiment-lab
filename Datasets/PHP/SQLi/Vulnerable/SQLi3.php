<?php
$search = $_POST['search'];
$query = "SELECT * FROM products WHERE name LIKE '%$search%'";
$result = mysqli_query($connection, $query);
?>