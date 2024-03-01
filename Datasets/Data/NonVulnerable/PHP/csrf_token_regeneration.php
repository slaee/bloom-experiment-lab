<?php
  session_start();

  if (!isset($_SESSION['csrf_token'])) {
    $_SESSION['csrf_token'] = bin2hex(random_bytes(32));
  }

  $token = $_SESSION['csrf_token'];
?>

<form action="process.php" method="post">
  <input type="hidden" name="csrf_token" value="<?php echo $token; ?>">
  <!-- Other form fields -->
  <input type="submit" value="Submit">
</form>
