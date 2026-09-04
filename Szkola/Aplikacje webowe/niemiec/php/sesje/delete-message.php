<?php

require_once "includes/utils.php";

session_start();

$db = connect_to_db();

$user_id = $_SESSION['user_id'];
$user= $db->query("SELECT * FROM users WHERE users.id = $user_id");
$user_role = $user->fetch_assoc()['ROLE'];
if ($user_role != "ROLE_ADMIN" && $user_role != "ROLE_MOD"){
    $_SESSION['error_message'] = "Nie masz uprawnień do tej akcji!";
    redirect("dashboard.php");
}

$message_id = $_GET["delete_id"] ?? "";

if ($message_id === "") {
    $_SESSION['error_message'] = "Nie można znaleźć tej wiadomości!";
    redirect("dashboard.php");
}

$result = $db->query("DELETE FROM chat WHERE id = '$message_id'");

if($result){
    $_SESSION['success_message'] = "Udało się usunąć wiadomość!";
    redirect("dashboard.php");
} else {
    $_SESSION['error_message'] = "Błąd po stronie serwera!";
    redirect("dashboard.php");
}
?>