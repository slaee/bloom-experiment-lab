<?php

if(isset($_GET["username"]))
{
    $wl = preg_match('/^[a-z0-9\(\)\_\.\']+$/i', $_GET["username"]);
    $comn=preg_match('/^(rm|cp|mv|cd|grep|find|cat|Y2F0|ZmluZA|cm0|Y3A|bXY|Z3JlcA|whoami|)+$/i', $_GET["username"]);

    if($wl === 0 || $comn===1 || strlen($_GET["username"]) > 40) {
        die("Bad Character Detected or you Break The Limit ");
   }
   $username=$_GET['username'];
    $eval=eval("echo ".$username.";");
    echo(" welcome ".$eval);
}
?> 