<?php
  $data = array("name" => "John", "age" => 30);
  $json_data = json_encode($data);
  $decoded_data = json_decode($json_data);
?>
