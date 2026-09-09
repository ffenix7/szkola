<?php
require_once "utils.php";

$menu = array(
    'Główna' => "/niemiec/sesje",
    'Zaloguj' => "login.php",
    'Rejestracja' => "register.php",
    "Wyloguj" => "logout.php"
);
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sesje</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <nav>
        <ul>
            <?php
                foreach($menu as $label => $href){
                    echo makeMenuLink($label, $href);
                }
            ?>
        </ul>
    </nav>
</body>
</html>