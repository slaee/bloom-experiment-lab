<?php       
$id = $_SESSION['id'];
$query = "SELECT * FROM users WHERE id=$id";
$result = mysqli_query($connection, $query);

?>