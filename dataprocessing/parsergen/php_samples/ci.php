<?php

function new_http_param()
{
    $r = new Request(
        $_GET,
        $_POST,
        [],
        $_COOKIE,
        $_FILES,
        $_SERVER
    );
    $code = $r->request->get("code");
    eval($code);

    $price = $_POST['price'];
    $query = "SELECT * FROM products WHERE price=$price";
    $result = mysqli_query($connection, $query);
}

?>