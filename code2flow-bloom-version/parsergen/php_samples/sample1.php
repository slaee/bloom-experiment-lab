<?php

$a = 'Simple string';
function query($a) {
    echo $a;
}
query($a);

$b = $_GET['q'];
$sql = `SELECT * FROM table WHERE id = ${b}`;

$test = $_SERVER['REMOTE_ADDR'];
if($_SERVER['REMOTE_ADDR'] == '127.0.0.1') {
    echo 'Localhost';
}

function SQLQuery($sql) {
    echo $sql;
}