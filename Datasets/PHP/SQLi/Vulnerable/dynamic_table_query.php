<?php
$table = $_GET['table'];
$query = "SELECT * FROM $table";
$result = mysqli_query($connection, $query);

?>