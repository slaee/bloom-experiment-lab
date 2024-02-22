<?php  
    /*  
    <flag> ➡➡➡ ⛳? ⬅⬅⬅ <flag>  
    */  
    if ($_SERVER['REQUEST_METHOD'] == 'POST'){  
        extract($_POST);  
      
        if (isset($_POST['password']) && md5($_POST['password']) == 'put hash here!'){  
            $loggedin = true;  
        }  
      
        if (md5($_SERVER['REMOTE_ADDR']) != '92d3fd4057d07f38474331ab231e1f0d'){  
        header('Location: ' . $_SERVER['REQUEST_URI']);  
        }  
          
        if (isset($loggedin) && $loggedin){  
            echo 'One step closer ?<br>';  
          
            if (isset($_GET['action']) && md5($_GET['action']) == $_GET['action']){  
                echo 'Really? ?<br>';  
                  
                $db = new SQLite3('database.db');  
                $sql_where = Array('1=0');  
                  
                foreach ($_POST as $key => $data) {  
                    $sql_where[] = $db->escapeString($key) . "='" . $db->escapeString($data) . "'";  
                }  
                  
                $result = $db->querySingle('SELECT login FROM users WHERE ' . implode(' AND ', $sql_where));  
                  
                if ($result == 'admin'){  
                    echo 'Last step ?<br>';  
                  
                    readfile(file_get_contents('php://input'));  
                }  
            }  
        }  
    }  
?> 