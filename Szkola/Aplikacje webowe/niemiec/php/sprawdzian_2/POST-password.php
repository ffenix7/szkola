<?php
require_once 'utils.php';
session_start();

if($_SESSION['email'] == null){
    header('Location: login.php');
}

$email = $_SESSION['email'];
$password = $_POST['password'];

$db = connect_to_db();

$result = $db->query("SELECT * FROM users WHERE email='$email' AND password='$password'");

if($result->fetch_assoc()){
    $_SESSION['session_id'] = uniqid();
    header('Location: welcome.php');
}
else{
    header('Location: password.php');
}