<?php
require_once "includes/header.php";
session_start();
?>

<?php
if(!empty($_SESSION["success_message"])){
    echo "<div class='success-message'>" . $_SESSION["success_message"] . "</div>";
}
?>

<?php
if(!empty($_SESSION["error_message"])){
    echo "<div class='error-message'>" . $_SESSION["error_message"] . "</div>";
}
?>

<form method="POST" action="post-login.php" class="standard-form">
    <label>
        Podaj login:
        <input type="text" name="login" placeholder="marian">
    </label><br>
    <label>
        Podaj hasło:
        <input type="password" name="password">
    </label><br>
    <button type="submit" value="Wyślij">Wyślij</button>
</form>

<?php
require_once "includes/footer.php";
?>