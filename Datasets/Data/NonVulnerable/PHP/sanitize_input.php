<?php
  $input = '<script>alert("XSS");</script>';
  $sanitized_input = htmlspecialchars($input, ENT_QUOTES, 'UTF-8');
  echo $sanitized_input;
?>
