<?php
// $user and $pass automatically set from POST request
if (login_user($user,$pass)) {
$authorized = true;
}


if ($authorized) {
generatePage();
}
?>
<?php
$user = $_POST['user'];
$pass = $_POST['pass'];
$authorized = false;
if (login_user($user,$pass)) {
$authorized = true;
}
?>
