<?php
  $stmt = $pdo->query("SELECT * FROM products");
  while ($row = $stmt->fetch()) {
    echo "Product: " . $row["product_name"] . ", Price: " . $row["price"] . "<br>";
  }
?>
