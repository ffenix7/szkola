<?php
require_once 'utils.php';
session_start();

$email = $_POST['email'];

if (str_contains($email, '@')){
    $_SESSION['email'] = $email;
    header('Location: password.php');
}

$db = connect_to_db();

$result = $db->query("SELECT * FROM users WHERE email='$email'");

if($result->fetch_assoc()){
    $_SESSION['email'] = $email;
    header('Location: password.php');
}
else{
    header('Location: register.php');
}