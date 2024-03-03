<?php
  session_start();

  if ($_POST['csrf_token'] === $_SESSION['csrf_token']) {
    // Process the form
    echo "Form processed successfully.";
  } else {
    echo "CSRF token verification failed.";
  }
?>
