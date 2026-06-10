<?php
require_once 'utils.php';

session_start();

if(!isset($_SESSION['email'])){
    header('Location: login.php');
}

$email = $_SESSION['email'];
$password = $_POST['password'];
$password_2 = $_POST['password_2'];


if($password != $password_2){
    header('Location: register.php');
}

if(strlen($password) < 6){
    header("Location: register.php");
}   

$db = connect_to_db();

$result = $db->query("INSERT INTO users (email, password) VALUES ('$email', '$password')");

if($result){
    $_SESSION['session_id'] = uniqid();
    header('Location: welcome.php');
}
else{
    header('Location: register.php');
}