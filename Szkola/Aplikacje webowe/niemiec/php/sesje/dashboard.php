<?php
    session_start();
    require_once "includes/header.php";
    require_once "includes/utils.php";
?>

<?php
if(!empty($_SESSION["success_message"])){
    echo "<div class='success-message'>" . $_SESSION["success_message"] . "</div>";
    unset($_SESSION["success_message"]);
}
?>

<?php
if(!empty($_SESSION["error_message"])){
    echo "<div class='error-message'>" . $_SESSION["error_message"] . "</div>";
    unset($_SESSION["error_message"]);
}
?>

<?php

?>

<h1>Dashboard</h1>

<form action="post-message.php" method="POST">
    <label>
        Wiadomość:
        <input type="textarea" name="message">
    </label><br>
    <button type="submit" value="submit" >Wyślij</button>
</form>

<?php
    $user_id = $_SESSION['user_id'];
    $db = connect_to_db();
    $user= $db->query("SELECT * FROM users WHERE users.id = $user_id");
    $user_role = $user->fetch_assoc()['ROLE'];
    if ($user_role == "ROLE_ADMIN"){
        echo "<p>" . "<a href='./panel.php'>Panel admina</a>" . "<br>";
    } 

    $results = $db->query("SELECT chat.id AS message_id, chat.message, chat.time, users.login, users.id AS user_id FROM chat JOIN users ON chat.user_id = users.id ORDER BY chat.id ASC");
    echo "<div class='chat'>";
    while($row = $results->fetch_assoc()){
            if ($user_role == "ROLE_ADMIN" || $user_role == "ROLE_MOD"){
            echo "<div class='message'>" . $row["login"] . ": " . $row["time"] . "<b>: " . $row["message"] . "<a class='delete' href='./delete-message.php?delete_id=" . $row["message_id"] . "'>X</a>" . "</b></div>";
        } 
        else{
            echo "<div class='message'>" . $row["login"] . ": " . $row["time"] . "<b>: " . $row["message"] . "</b></div>";
        }
    }
    echo "</div>";

?>

<?php
    require_once "includes/footer.php"
?>