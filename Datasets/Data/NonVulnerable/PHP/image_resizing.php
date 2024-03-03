<?php
  $image = imagecreatefromjpeg('input.jpg');
  $resized = imagescale($image, 100, 100);
  imagejpeg($resized, 'output.jpg');
?>
