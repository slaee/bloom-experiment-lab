<?php
$id = $user_id;
$query = "SELECT * FROM users WHERE id='$id'";
$result = mysqli_query($connection, $query);
?>