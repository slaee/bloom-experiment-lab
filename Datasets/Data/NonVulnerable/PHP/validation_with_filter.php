<?php
  $url = "http://www.example.com";
  if (filter_var($url, FILTER_VALIDATE_URL)) {
    echo "Valid URL";
  } else {
    echo "Invalid URL";
  }
?>
