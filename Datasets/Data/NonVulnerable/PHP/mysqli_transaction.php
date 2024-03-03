<?php
  $conn = new mysqli('localhost', 'user', 'password', 'database');

  $conn->autocommit(false);

  $sql1 = "UPDATE accounts SET balance = balance - 50 WHERE user_id = 123";
  $sql2 = "UPDATE products SET stock = stock - 1 WHERE product_id = 456";

  $conn->query($sql1);
  $conn->query($sql2);

  $conn->commit();
  $conn->close();
?>
