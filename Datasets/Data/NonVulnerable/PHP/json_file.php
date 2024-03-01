<?php
  $json_data = '{"name": "Alice", "age": 28}';
  $data = json_decode($json_data, true);
  echo "Name: " . $data['name'];
?>
