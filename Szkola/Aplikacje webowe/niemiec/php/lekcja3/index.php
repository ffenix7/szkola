<?php
class Table{
    private $table = [];
    public $words = [];
    private $export = "";
    public function __construct($n, $m){
        for($i=0;$i<$n;$i++){
            for($j=0;$j<$m;$j++){
                $this->table[$i][$j] = "dupa";
            }
        }
    }
    public function toHTML(){
        $this->export .= "<table>";
        for($i=0;$i<count($this->table);$i++){
            $this->export .= "<tr>";
            for($j=0;$j<count($this->table[$i]);$j++){
                $this->export .= "<td>" . $this->table[$i][$j] . "</td>";
            }
            $this->export .= "</tr>";
        }
        $this->export .= "</table>";
        return $this->export;
    }

    public function setValue($x, $y, $val){
        $this->table[$x-1][$y-1] = $val;
    }

    public function randomizeNumbers(){
        for($i=0;$i<count($this->table);$i++){
            for($j=0;$j<count($this->table[$i]);$j++){
                $this->table[$i][$j] = rand();
            }
        }
    }

    public function randomizeLetters(){
        for($i=0;$i<count($this->table);$i++){
            for($j=0;$j<count($this->table[$i]);$j++){
                $this->table[$i][$j] = chr(rand(0,25) + 65);
            }
        }
    }

    public function generate_crossword(){
        $used = array();
        for($i=0;$i<count($this->words);$i++){
            $len = strlen($this->words[$i]);
            $horizontal = rand(0,1) === 1;
            if($horizontal){
                $x = rand(0, count($this->table[0]) - $len);
                $y = rand(0, count($this->table) - 1);
                for($j=0;$j<$len;$j++){
                    if(isset($used[$y][$x+$j]) && $used[$y][$x+$j]){
                        continue 2;
                    }
                }
                for($j=0;$j<$len;$j++){
                    $this->table[$y][$x+$j] = $this->words[$i][$j];
                    $used[$y][$x+$j] = true;
                }
            }
            else{
                $x = rand(0, count($this->table[0]) - 1);
                $y = rand(0, count($this->table) - $len);
                for($j=0;$j<$len;$j++){
                    if(isset($used[$y+$j][$x]) && $used[$y+$j][$x]){
                        continue 2;
                    }
                }
                for($j=0;$j<$len;$j++){
                    $this->table[$y+$j][$x] = $this->words[$i][$j];
                    $used[$y+$j][$x] = true;
                }
            }
        }
    }
}

$words = [];
if (isset($_POST['words'])) {
    $input = trim($_POST['words']);
    if (!empty($input)) {
        $words = array_map('strtoupper', array_map('trim', explode(',', $input)));
    }
}

$table = new Table(10, 10);
if (!empty($words)) {
    $table->words = $words;
}
$table->randomizeLetters();
$table->generate_crossword();

echo $table->toHTML();
?>

<!DOCTYPE html>
<html lang="pl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Wykreślanki</title>
    <style>
        table{
            display: flex;
            flex-direction: center;
            justify-content: space-evenly;
            margin-top: 10%;
        }
        td{
            border: 1px solid black;
            text-align: center;
            padding: 10px;
            transition: 3s;
        }
        td:hover{
            transition: 0.1s;
            background-color: red;
        }
    </style>
</head>
<body>
    
</body>
<div style="display: flex; flex-direction: column; align-items: center; margin-top: 30px;">
    <form method="POST" style="margin-bottom: 20px;">
        <label for="words">Wpisz słowa:</label><br>
        <input type="text" id="words" name="words" style="width: 300px;" placeholder="kot, pies">
        <button type="submit">Generuj krzyżówkę</button>
    </form>
</div>
</html>