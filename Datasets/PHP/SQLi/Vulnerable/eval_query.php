<?php
$id = $_GET['id'];
eval("\$query = \"SELECT * FROM products WHERE id=$id\";");
$result = mysqli_query($connection, $query);

?>