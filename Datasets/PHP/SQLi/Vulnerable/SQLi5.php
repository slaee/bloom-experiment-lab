<?php
$id = $_POST['id'];
$query = "SELECT * FROM products WHERE id='$id'";
$result = mysqli_query($connection, $query);
?>