<?php
  if ($_FILES["file"]["error"] == 0 && $_FILES["file"]["type"] == "image/jpeg") {
    move_uploaded_file($_FILES["file"]["tmp_name"], "uploads/" . $_FILES["file"]["name"]);
    echo "File uploaded successfully.";
  } else {
    echo "Invalid file format or upload error.";
  }
?>
