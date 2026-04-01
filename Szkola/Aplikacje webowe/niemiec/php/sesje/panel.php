<?php

require_once "includes/header.php";
require_once "includes/utils.php";

session_start();

?>

<h2>Panel admina</h2>
<a href="./dashboard.php">Dashboard</a>

<?php
$db = connect_to_db();

$user_id = $_SESSION['user_id'];
$is_admin = $db->query("SELECT users.role FROM users WHERE users.id = $user_id");
if (!$is_admin->fetch_assoc() == "ROLE_ADMIN"){
    $_SESSION['error_message'] = "Nie masz uprawnień do tej strony!";
    redirect("dashboard.php");
}

$result = $db->query("SELECT * FROM users");

echo "<table>";
echo "<tr>" . "<th>ID</th>" . "<th>Login</th>" . "<th>Rola</th>" . "</tr>";

while($row = $result->fetch_assoc()){
    $row_user_id = $row['id'];
    $row_login = $row['login'];
    $row_role = $row['ROLE'];
    echo "<tr>" . "<td>$row_user_id</td>" . "<td>$row_login</td>" . "<td>$row_role</td>" .  "<td><a class='delete' href='./delete-user.php?id=$row_user_id'>X</a></td>" . "<td><a href='./admin.php?id=$row_user_id'>Admin</a> <a href='./moderator.php?id=$row_user_id'>Moderator</a> <a href='user.php?id=$row_user_id'>User</a></td>" . "</tr>";
}
echo "</table>";

?>

<?php

require_once "includes/footer.php";

?>