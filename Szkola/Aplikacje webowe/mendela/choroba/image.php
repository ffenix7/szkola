<?php
$db = mysqli_connect("localhost", "root", "ServBay.dev", "choroby");

$result = $db->query("SELECT * FROM data"); // zmień data na temperatura lub zmień nazwę tabeli

$baseWidth = 1000;
$baseHeight = 600;
$width = $_GET['width'] ?? $baseWidth;
$height = $_GET['height'] ?? $baseHeight;

$marginLeft = 150;
$marginRight = 150;
$marginTop = 100;
$marginBottom = 150;

$plotRight = $width - $marginRight;
$plotBottom = $height - $marginBottom;
$plotWidth = max(1, $plotRight - $marginLeft);
$plotHeight = max(1, $plotBottom - $marginTop);
$xStep = $plotWidth / 28;
$labelFont = 5;
$smallFont = 2;
$tickFont = 2;
$dotSize = 6;

header('Content-Type: image/png');
$im = imagecreatetruecolor($width, $height);

define("BL", imagecolorallocate($im, 0, 0, 0));
define("RED", imagecolorallocate($im, 255, 0, 0));
define("BLUE", imagecolorallocate($im, 0, 0, 255));
define("GRAY", imagecolorallocate($im, 200, 200, 200));
define("WHITE", imagecolorallocate($im, 255, 255, 255));

imagefilledrectangle($im, 0, 0, $width, $height, WHITE);

imagesetstyle($im, [BL]);
imageline($im, $marginLeft, $plotBottom, $plotRight, $plotBottom, IMG_COLOR_STYLED);


imagesetstyle($im, [BL]);
imageline($im, $marginLeft, $marginTop, $marginLeft, $plotBottom, IMG_COLOR_STYLED);

imagestring($im, $labelFont, $marginLeft + ($plotWidth - imagefontwidth($labelFont) * strlen("dzien pomiaru")) / 2, $plotBottom + $marginBottom * 0.33, "dzien pomiaru", BL);
imagestringup($im, $labelFont, max(0, $marginLeft - $marginLeft * 0.4), $marginTop + $plotHeight / 2 + imagefontwidth($labelFont) * strlen("temperatura") / 2, "temperatura", BL);

//os x
for($i=1; $i< 29; $i++){
    imagesetstyle($im, [BL]);
    $x = $marginLeft + $i * $xStep;
    imageline($im, $x, $plotBottom - 5, $x, $plotBottom + 5, IMG_COLOR_STYLED);
    imagestring($im, $smallFont, $x - imagefontwidth($smallFont) * strlen((string) $i) / 2, $plotBottom + 7, $i, BL);
}

//przerywane x
for($i=1; $i< 29; $i++){
    imagesetstyle($im, [GRAY, GRAY, WHITE, WHITE]);
    $x = $marginLeft + $i * $xStep;
    imageline($im, $x, $marginTop, $x, $plotBottom, IMG_COLOR_STYLED);
}

//przerywane y
for($i=0; $i< 10; $i++){
    imagesetstyle($im, [GRAY, GRAY, WHITE, WHITE]);
    $y = $marginTop + $i * $plotHeight / 10;
    imageline($im, $marginLeft, $y, $plotRight, $y, IMG_COLOR_STYLED);
}

//mala os y
$temp = 38.0;
for($i= 0; $i< 10; $i++){
    imagesetstyle($im, [BL]);
    $y = $marginTop + $i * $plotHeight / 10;
    imageline($im, $marginLeft - 5, $y, $marginLeft + 5, $y, IMG_COLOR_STYLED);
    imagestring($im, $tickFont, $marginLeft - $marginLeft * 0.2, $y - imagefontheight($tickFont) / 2, $temp, BL);
    $temp -= 0.2;
}

//czerwona linia
$redLineY = $marginTop + $plotHeight / 2;
imageline($im, $marginLeft, $redLineY, $plotRight, $redLineY, RED);

//kropy
$dots_ill = [];
$dots_healthy = [];
while($row = $result->fetch_assoc()){
    imagesetstyle($im, [BL]);
    $y = $plotBottom - (($row['value'] - 36.0) / 2.0) * $plotHeight;
    $x = $marginLeft + $row['day'] * $xStep;
    if ($row['ill'] == true){
        array_push($dots_healthy, [$x, $y]);
    }
    else{
        array_push($dots_ill, [$x, $y]);
    }
    imagefilledellipse($im, $x, $y, $dotSize, $dotSize, $row['ill'] == true ? RED : BLUE);
}

//linie między kropkami
for($i=0;$i<sizeof($dots_healthy)-1;$i++){
    imagesetstyle($im, [BL]);
    imageline($im, $dots_healthy[$i][0], $dots_healthy[$i][1], $dots_healthy[$i+1][0], $dots_healthy[$i+1][1], RED);
}

for($i=0;$i<sizeof($dots_healthy)-1;$i++){
    imagesetstyle($im, [BL]);
    imageline($im, $dots_ill[$i][0], $dots_ill[$i][1], $dots_ill[$i+1][0], $dots_ill[$i+1][1], BLUE);
}

imagepng($im);