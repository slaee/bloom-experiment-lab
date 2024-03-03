<?php
  session_start();

  $timeout = 30 * 60; // 30 minutes
  $last_activity = $_SESSION['last_activity'];

  if (time() - $last_activity > $timeout) {
    session_unset();
    session_destroy();
    echo "Session expired. Please log in again.";
  } else {
    $_SESSION['last_activity'] = time();
    echo "User is still active.";
  }
?>
