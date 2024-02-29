<?php
$username = $_GET['username'];
echo '<div class="header"> Welcome, ' . $username . '</div>';
?>
<?php
$username = mysql_real_escape_string($username);
$fullName = mysql_real_escape_string($fullName);
$query = sprintf('Insert Into users (username,password) Values ("%s","%s","%s")', $username, crypt($password),$fullName) ;
mysql_query($query);
?>
<?php
$query = 'Select * From users Where loggedIn=true';
$results = mysql_query($query);

if (!$results) {
exit;
}

//Print list of users to page
echo '<div id="userlist">Currently Active Users:';
while ($row = mysql_fetch_assoc($results)) {
echo '<div class="userNames">'.$row['fullname'].'</div>';
}
echo '</div>';
?>
<?php
$name = $_COOKIE["myname"];
$announceStr = "$name just logged in.";

//save HTML-formatted message to file; implementation details are irrelevant for this example.
saveMessage($announceStr);
?>
