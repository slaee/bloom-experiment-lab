<?php
  $user_id = $_GET['user_id'];
  $page = isset($_GET['page']) ? $_GET['page'] : 1;
  echo "User ID: $user_id, Page: $page";
?>

