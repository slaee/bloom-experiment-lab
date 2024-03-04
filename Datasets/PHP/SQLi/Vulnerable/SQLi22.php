<?php
$email = $userEmail;
$query = "SELECT * FROM users WHERE email='$email'";
$result = mysqli_query($connection, $query);
?>