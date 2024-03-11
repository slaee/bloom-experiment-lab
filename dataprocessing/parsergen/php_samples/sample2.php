<?php
$id = $_GET['id'];
$query = "SELECT * FROM products WHERE id=$id";
$result = mysqli_query($connection, $query);

