<?php
  $file = 'document.pdf';
  header('Content-Type: application/pdf');
  header('Content-Disposition: attachment; filename="' . basename($file) . '"');
  readfile($file);
?>
