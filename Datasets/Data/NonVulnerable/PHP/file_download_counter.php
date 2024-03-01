<?php
  $file = 'document.pdf';
  header('Content-Type: application/pdf');
  header('Content-Disposition: attachment; filename="' . basename($file) . '"');
  header('X-Accel-Redirect: /download/' . basename($file));
  echo "File download initiated.";
?>
