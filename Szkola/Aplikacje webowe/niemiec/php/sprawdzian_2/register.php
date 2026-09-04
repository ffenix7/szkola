<?php

session_start();

if (!isset($_SESSION['email'])){
    header('Location: login.php');
}

$email = $_SESSION['email'];

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <header>
        <p>
            Nie ma jeszcze konta dla <?= $_SESSION['email'] ?>, zarejestruj się!
        </p>
    </header>
    <form method="POST" action="POST-register.php">
        Hasło: <input type="password" value="password">
        Powtórz hasło: <input type="password" value="password_2">
        <button type="submit">Zarejestruj</button>

    </form>
</body>
</html>