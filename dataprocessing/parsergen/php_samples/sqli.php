<?php
$price = $_POST['price'];
$query = "SELECT * FROM products WHERE price=$price";
$result = mysqli_query($connection, $query);

?>