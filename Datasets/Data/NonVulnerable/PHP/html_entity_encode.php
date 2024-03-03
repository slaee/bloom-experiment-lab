<?php
  $input = '<script>alert("XSS");</script>';
  $encoded_input = htmlentities($input, ENT_QUOTES, 'UTF-8');
  echo $encoded_input;
?>
