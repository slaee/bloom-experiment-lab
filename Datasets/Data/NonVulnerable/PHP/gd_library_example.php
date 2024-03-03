<?php
  $img = imagecreatetruecolor(200, 200);
  $bg_color = imagecolorallocate($img, 255, 255, 255);
  imagefilledrectangle($img, 0, 0, 200, 200, $bg_color);
  header('Content-Type: image/png');
  imagepng($img);
  imagedestroy($img);
?>
