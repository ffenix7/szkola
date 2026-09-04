<?php
require_once "includes/utils.php";
session_start();

unset($_SESSION['error_message']);
unset($_SESSION['success_message']);

if (empty($_POST["login"])){
    $_SESSION['error_message'] = "Musisz podać login!";
    redirect("register.php");
}

if (empty($_POST["password"])){
    $_SESSION['error_message'] = "Musisz podać hasło!";
    redirect("register.php");
}

if (empty($_POST["password2"])){
    $_SESSION['error_message'] = "Musisz powtórzyć hasło!";
    redirect("register.php");
}

if($_POST["password"] != $_POST["password2"]){
    $_SESSION['error_message'] = "Hasła muszą być takie same!";
    redirect("register.php");
}

$db = connect_to_db();

$login = $_POST["login"];
$pass = password_hash($_POST["password"], PASSWORD_DEFAULT);

$check_login = $db->query("SELECT * FROM users WHERE users.login = '$login'");
if($check_login->fetch_assoc()['login']){
    $_SESSION['error_message'] = "Istnieje już użytkownik o takim loginie!";
    redirect("register.php");
}

$result = $db->query("INSERT INTO users (`login`, `password`) VALUES ('$login', '$pass')");

if(!$result){
    $_SESSION['error_message'] = "Błąd po stronie serwera!";
    redirect("register.php");
}

$_SESSION['success_message'] = "Udało się zarejestrować! Teraz możesz się zalogować";
redirect("login.php");