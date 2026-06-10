<?php

function connect_to_db(){
    return new mysqli('lcoalhost', 'root', '', 'sprawdzian_2');
}