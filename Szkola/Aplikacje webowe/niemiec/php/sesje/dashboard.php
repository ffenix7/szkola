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

    $db = connect_to_db();

    $results = $db->query("SELECT * FROM chat JOIN users ON chat.user_id = users.id ORDER BY chat.id ASC");
    echo "<div class='chat'>";
    while($row = $results->fetch_assoc()){
        echo "<div class='message'>" . $row["login"] . ": " . $row["time"] . "<b>: " . $row["message"] . "</b></div>";
    }
    echo "</div>";

?>

<?php
    require_once "includes/footer.php"
?>