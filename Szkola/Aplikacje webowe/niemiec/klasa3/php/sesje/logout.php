<?php
require_once "includes/utils.php";

session_start();
unset($_SESSION["user_id"]);
$_SESSION["success_message"] = "Udało się wylogować!";


redirect("login.php");