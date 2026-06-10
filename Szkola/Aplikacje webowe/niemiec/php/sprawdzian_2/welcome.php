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
            Witaj, <?= $_SESSION['email'] ?>!
        </p>
        <p>
            <a href="logout.php">Wyloguj się
            </a>
        </p>
    </header>
</body>
</html>