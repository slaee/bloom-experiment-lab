<?php
$id = $userID;
$query = "SELECT * FROM users WHERE id='$id'";
$result = mysqli_query($connection, $query);
?>