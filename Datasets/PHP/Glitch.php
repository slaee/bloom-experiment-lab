// conf.php

<?php
$dbhost="localhost";
$dbuser="x";
$dbpass="x";
$dbname="x";

$con = mysqli_connect($dbhost, $dbuser, $dbpass, $dbname);


if (!function_exists('getAUTHkey') ){
	function getAUTHkey($user){
		global $con;
		$sql = mysqli_query($con,"SELECT k3y FROM tab WHERE user='".mysqli_real_escape_string($con,$user)."' ") ;
		return @mysqli_fetch_assoc($sql)['k3y'];
	}
}

if (!function_exists('bake_cookie') ){
	function bake_cookie($user){
		$AUTH_SECRET=getAUTHkey($user['user']);
		$encrypted=encrypt_msg($user['user']."|".$user['password'],$AUTH_SECRET);
		$hmac=hmac_sign($encrypted,$AUTH_SECRET);
		return base64_encode($hmac."-".$encrypted);
	}
}

if (!function_exists('encrypt_msg') ){
	function encrypt_msg( $plain,$key ) {
		$cipher="AES-256-ECB";
		$ivlen = openssl_cipher_iv_length($cipher);
	    $iv = openssl_random_pseudo_bytes($ivlen);
	    $encrypted = openssl_encrypt($plain, $cipher, $key, $options=0, $iv);
		return trim( base64_encode( $encrypted ) );
	}
}

if (!function_exists('decrypt_msg') ){
	function decrypt_msg( $encrypted,$key ) {
		$cipher="AES-256-ECB";
		$ivlen = openssl_cipher_iv_length($cipher);
	    $iv = openssl_random_pseudo_bytes($ivlen);
		$decrypted = openssl_decrypt(base64_decode($encrypted), $cipher, $key, $options=0, $iv);
		return trim( $decrypted );
	}
}

if (!function_exists('hmac_sign') ){
	function hmac_sign($message, $key)	{
	    return hash_hmac('sha256', $message, $key);
	}
}


if (!function_exists('hmac_verify') ){
	function hmac_verify($bundle, $key)	{
		$bundle=base64_decode($bundle);
	    $msgMAC = mb_substr($bundle, 0, 64, '8bit');
	    $message = mb_substr($bundle, 65, null, '8bit');
	    return hash_equals(
	        hmac_sign($message, $key),
	        $msgMAC
	    );
	}
}

if (!function_exists('isLogged') ){
	function isLogged($Auth,$User){
		global $con;
		$sql = mysqli_query($con,"SELECT * FROM tab WHERE user='".mysqli_real_escape_string($con,$User)."' ") ;
		if(mysqli_num_rows($sql)!==0){
			$AuthKey=getAUTHkey($User);
			if(hmac_verify($Auth,$AuthKey)) {
				$bundle=base64_decode($Auth);
			    $message = mb_substr($bundle, 65, null, '8bit');
			    $userData=explode("|",decrypt_msg($message,$AuthKey) );
			    include 'GLITCH/getSecrets.php';
				return array('OK',$qwertyuiop[$userData[0]]);
			}
		}
		return array('NO','');
	}
}

if (!function_exists('authenticate') ){
	function authenticate($usr,$pw){
		global $con;
		$sql = mysqli_query($con,"SELECT * FROM tab WHERE user='".mysqli_real_escape_string($con,$usr)."' AND password='".mysqli_real_escape_string($con,$pw)."' ") ;
		if (mysqli_num_rows($sql)!==0){
			return mysqli_fetch_array($sql);
		} else {
			return FALSE;
		}
	}
}

if (!function_exists('out') ){
	function out($array=array()){
		die(json_encode($array));
	}
}
?>

<?php
include 'conf.php';


if(@$_POST['usr'] AND @$_POST['pw']){
	if($auth=authenticate($_POST['usr'],$_POST['pw'])){
		$msg='login success';
		$AuthCookie=bake_cookie($auth);
		out(array(
			$msg,$AuthCookie,$auth['user']
		));
	}else{
		$msg='login failed';
		out(array(
			$msg
		));
	}
}

if(@$_POST['Auth'] AND @$_POST['User']){
	out(isLogged($_POST['Auth'],$_POST['User']));
}


echo 'end';