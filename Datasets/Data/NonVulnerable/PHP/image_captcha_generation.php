<?php
  $image = imagecreatetruecolor(100, 40);
  $text_color = imagecolorallocate($image, 255, 255, 255);
  $captcha_text = rand(1000, 9999);
  $_SESSION['captcha'] = $captcha_text;
  imagestring($image, 5, 10, 10, $captcha_text, $text_color);
  header('Content-Type: image/png');
  imagepng($image);
  imagedestroy($image);
?>
