<?php
$name = $_SERVER['HTTP_X_NAME'];
$query = "SELECT * FROM users WHERE name='$name'";
$result = mysqli_query($connection, $query);

?>