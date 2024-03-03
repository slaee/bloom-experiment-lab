<?php
$username = addslashes($_POST['username']);
$password = addslashes($_POST['password']);
$query = "SELECT * FROM users WHERE username='$username' AND password='$password'";
$result = mysqli_query($connection, $query);

?>