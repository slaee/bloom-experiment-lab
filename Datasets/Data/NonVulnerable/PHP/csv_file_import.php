<?php
  if ($_FILES["file"]["error"] == 0 && $_FILES["file"]["type"] == "text/csv") {
    $csv_data = array_map('str_getcsv', file($_FILES["file"]["tmp_name"]));
    foreach ($csv_data as $row) {
      echo "Name: $row[0], Age: $row[1], City: $row[2] <br>";
    }
  } else {
    echo "Invalid file format or upload error.";
  }
?>
