<?php
$start = $_GET['start'];
$limit = $_GET['limit'];
$query = "SELECT * FROM products LIMIT $start, $limit";
$result = mysqli_query($connection, $query);

?>