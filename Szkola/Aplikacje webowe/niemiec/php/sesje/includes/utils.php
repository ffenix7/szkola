<?php

function makeMenuLink($label, $href){
    return '<li><a class="menu-link" href="' . $href . '">' . $label . '</a></li>';  
}

function connect_to_db(){
    return new mysqli('localhost', 'root', '', 'chat');
}

function redirect($target){
    header('Location: ' . $target);
    exit();
}