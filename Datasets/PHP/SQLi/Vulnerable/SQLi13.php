<?php
$username = $_POST['username'];
$query = "SELECT * FROM users WHERE username='$username'";
$result = mysqli_query($connection, $query);
?>