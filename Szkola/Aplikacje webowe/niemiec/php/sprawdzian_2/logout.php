<?php

session_start();
session_destroy();
unset($_SESSION['email']);
unset($_SESSION['session_id']);
header('Location: login.php');