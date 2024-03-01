<?php
  $file = fopen("example.txt", "w");
  fwrite($file, "This is a sample text.");
  fclose($file);
?>
