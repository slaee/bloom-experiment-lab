<?php
  session_start();

  $token = md5(uniqid(rand(), TRUE));
  $_SESSION['csrf_token'] = $token;
?>

<form action="process.php" method="post">
  <input type="hidden" name="csrf_token" value="<?php echo $token; ?>">
  <!-- Other form fields -->
  <input type="submit" value="Submit">
</form>
