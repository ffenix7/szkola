<?php

$db = mysqli_connect("localhost", "root", "ServBay.dev", "choroby");

$result = $db->query("SELECT * FROM temperatura");

$row = $result->fetch_assoc();
