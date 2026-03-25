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

$db = connect_to_db();

$login = $_POST["login"];
$pass = $_POST["password"];

$result = $db->query("SELECT users.password FROM users WHERE users.login = '$login'");
$hash = $result->fetch_assoc()['password'];

if(!$hash){
    $_SESSION['error_message'] = "Nie znaleziono takiego loginu!";
    redirect("login.php");
}

if(password_verify($pass, $hash)){
    $_SESSION['success_message'] = "Udało się zalogować!";
    $_SESSION["user_id"] = $db->query("SELECT users.id FROM users WHERE users.login = '$login'")->fetch_assoc()['id'];
    redirect("dashboard.php");
}

else{
    $_SESSION['error_message'] = "Niepoprawne hasło lub login!";
    redirect("login.php");
}
