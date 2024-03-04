<?php
$name = $_POST['name'];
$query = "SELECT * FROM users WHERE name='$name'";
$result = mysqli_query($connection, $query);
?>