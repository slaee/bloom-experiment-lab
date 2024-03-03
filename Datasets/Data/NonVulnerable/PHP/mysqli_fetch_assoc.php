<?php
  $result = $conn->query("SELECT * FROM products");
  while ($row = $result->fetch_assoc()) {
    echo "Product: " . $row["product_name"] . ", Price: " . $row["price"] . "<br>";
  }
?>
