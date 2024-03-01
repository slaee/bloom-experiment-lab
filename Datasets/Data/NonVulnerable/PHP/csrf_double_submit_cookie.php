<?php
  session_start();
  $token = bin2hex(random_bytes(32));
  $_SESSION['csrf_token'] = $token;

  setcookie('csrf_cookie', $token, time() + 3600, '/');
?>

<form action="process.php" method="post">
  <input type="hidden" name="csrf_token" value="<?php echo $token; ?>">
  <!-- Other form fields -->
  <input type="submit" value="Submit">
</form>
