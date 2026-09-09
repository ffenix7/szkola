<!DOCTYPE html>
<html lang="pl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        td{
            border: 1px solid black;
        }
    </style>
</head>
<body>
    <form method="GET">
        <input placeholder="name" name="name">
        <input placeholder="price_per_kg" name="price_per_kg">
        <input placeholder="stock" name="stock">
        <button type="submit" >Wyślij</button>
    </form>
</body>
</html>

<?php
$db = mysqli_connect('localhost', 'root', '', 'groceries');

if(!$db){
    echo'Nie udało się połączyć';
    exit;
}
else{
    echo 'Udało się połączyć';
}

echo "<br>";

if(isset($_GET['delete-item'])){
    $id = $_GET['delete-item'];
    $res = mysqli_query($db,"DELETE FROM products WHERE id='" . $id . "';");
    }
    
    #READ
$res = mysqli_query($db, "SELECT * FROM products;");

echo "<table>";
while($product = mysqli_fetch_assoc($res)){
    echo "<tr>";    
    echo "<td>" . $product['name'] . "</td>";
    echo "<td>" . $product['price_per_kg'] . "</td>";
    echo "<td>" . $product['stock'] . "</td>";
    echo "<td>" .'<a href="?edit-item=' . $product['id'] .'">edytuj </a></td>';
    echo "<td>" .'<a href="?delete-item=' . $product['id'] .'">usuń </a></td>';
    
    echo "</tr>";
    }    
echo "</table>";

#DELETE
#$res = mysqli_query($db, "DELETE FROM products where id=1");

#CREATE

if(isset($_GET['name'])){
    $name = $_GET['name'];
    $price_per_kg = $_GET['price_per_kg'];
    $stock = $_GET['stock'];
    $res_create = mysqli_query($db, "INSERT INTO products (`id`, `name`, `price_per_kg`, `stock`) VALUES (NULL, '$name', '$price_per_kg', '$stock');");
}

#UPDATE


?>