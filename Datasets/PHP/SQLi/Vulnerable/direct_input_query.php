<?php
$query = "SELECT * FROM users WHERE id=" . $_GET['id'];
$result = mysqli_query($connection, $query);

?>