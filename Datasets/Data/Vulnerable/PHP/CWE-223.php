<?php
function login($userName,$password){
if(authenticate($userName,$password)){
return True;
}
else{
incrementLoginAttempts($userName);
if(recentLoginAttempts($userName) > 5){
writeLog("Failed login attempt by User: " . $userName . " at " + date('r') );
}
}
}
?>
<?php
function readFile($filename){
$user = getCurrentUser();
$realFile = $filename;

//resolve file if its a symbolic link
if(is_link($filename)){
$realFile = readlink($filename);
}

if(fileowner($realFile) == $user){
echo file_get_contents($realFile);
return;
}
else{
echo 'Access denied';
writeLog($user . ' attempted to access the file '. $filename . ' on '. date('r'));
}
}
?>
