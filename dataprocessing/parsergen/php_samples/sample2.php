<?php

$a = 'Simple string';
function query($a) {
    echo $a;
}
query($a);

$b = $_GET['q'];
$sql = `SELECT * FROM table WHERE id = ${b}`;

if($_SERVER['REQUEST_METHOD'] === 'POST') {
    $c = $_POST['c'];
    $sql = `SELECT * FROM table WHERE id = ${c}`;
}

function SQLQuery($sql) {
    echo $sql;
}


?>