<?php
$username = $_POST['username'];
$password = $_POST['password'];
$query = "SELECT * FROM users WHERE (username=? OR email=?) AND password=?";
$stmt = mysqli_prepare($connection, $query);
mysqli_stmt_bind_param($stmt, "sss", $username, $username, $password);
mysqli_stmt_execute($stmt);
$result = mysqli_stmt_get_result($stmt);

?>