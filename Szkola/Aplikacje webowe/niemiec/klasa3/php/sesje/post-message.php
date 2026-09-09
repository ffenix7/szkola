<?php
require_once "includes/utils.php";
session_start();

unset($_SESSION['error_message']);
unset($_SESSION['success_message']);


$db = connect_to_db();

if (empty($_SESSION["user_id"])) {
    $_SESSION['error_message'] = "Musisz być zalogowany!";
    redirect("login.php");
}

$user_id = $_SESSION["user_id"];
$message = trim($_POST["message"] ?? "");

if ($message === "") {
    $_SESSION['error_message'] = "Wiadomość nie może być pusta!";
    redirect("dashboard.php");
}

$result = $db->query("INSERT INTO chat (`user_id`, `message`) VALUES ('$user_id', '$message')");

if(!$result){
    $_SESSION['error_message'] = "Błąd po stronie serwera!";
    redirect("dashboard.php");
}

$_SESSION['success_message'] = "Udało się dodać wiadomość!";
redirect("dashboard.php");