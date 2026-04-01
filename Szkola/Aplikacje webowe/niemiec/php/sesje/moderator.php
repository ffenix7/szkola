<?php

require_once "includes/utils.php";

session_start();

$db = connect_to_db();

$is_admin = $db->query("SELECT users.role FROM users WHERE users.id = " . $_SESSION['user_id']);
if (!$is_admin->fetch_assoc() == "ROLE_ADMIN"){
    $_SESSION['error_message'] = "Nie masz uprawnień do tej strony!";
    redirect("dashboard.php");
}

$user_id = $_GET['id'];

$result = $db->query("UPDATE users SET role = 'ROLE_MOD' WHERE id = $user_id");

if($result){
    $_SESSION['success_message'] = "Użytkownik został zmieniony!";
    redirect("panel.php");
} else {
    $_SESSION['error_message'] = "Coś poszło nie tak!";
    redirect("panel.php");
}

?>