<?php
session_start();

if (!isset($_SESSION['email'])){
    header('Location: login.php');
}

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
            Logujesz się jako <?= $_SESSION['email'] ?>
        </p>
    </header>
    <form method="POST" action="POST-password.php">
        Hasło: <input type="password" value="password">
        <button type="submit">Zaloguj</button>
    </form>
</body>
</html>