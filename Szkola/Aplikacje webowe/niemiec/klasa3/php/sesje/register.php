<?php
require_once "includes/header.php";
?>

<?php
session_start();
?>

<h1>Zarejestruj się</h1>

<?php
if(!empty($_SESSION["error_message"])){
    echo "<div class='error-message'>" . $_SESSION["error_message"] . "</div>";
}
?>

<form method="POST" action="post-register.php" class="standard-form">
    <label>
        Podaj login:
        <input type="text" name="login" placeholder="marian">
    </label><br>
    <label>
        Podaj hasło:
        <input type="password" name="password">
    </label><br>
    <label>
        Powtórz hasło:
        <input type="password" name="password2">
    </label><br>
    <button type="submit" value="Wyślij">Wyślij</button>
</form>

<?php

require_once "includes/footer.php";