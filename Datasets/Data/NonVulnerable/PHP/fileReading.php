<?php
  $file = fopen("example.txt", "r");
  echo fread($file, filesize("example.txt"));
  fclose($file);
?>
