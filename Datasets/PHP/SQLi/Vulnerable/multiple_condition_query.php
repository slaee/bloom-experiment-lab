<?php
$username = $_POST['username'];
$password = $_POST['password'];
$query = "SELECT * FROM users WHERE username='$username' OR email='$username' AND password='$password'";
$result = mysqli_query($connection, $query);

?>