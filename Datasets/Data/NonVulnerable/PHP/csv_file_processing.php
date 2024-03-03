<?php
  $csv_file = fopen('data.csv', 'r');
  while (($data = fgetcsv($csv_file)) !== FALSE) {
    echo "Name: $data[0], Age: $data[1] <br>";
  }
  fclose($csv_file);
?>
