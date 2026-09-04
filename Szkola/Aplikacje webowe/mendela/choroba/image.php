<?php
header('Content-Type: image/png');
$im = imagecreatetruecolor(1000, 600);
$white = imagecolorallocate($im, 255, 255, 255);
imagefilledrectangle($im, 0, 0, 1000, 600, $white);
define("BL", imagecolorallocate($im, 0, 0, 0));
define("GRAY", imagecolorallocate($im, 200, 200, 200));

imagesetstyle($im, [BL]);
imageline($im, 150, 450, 800, 450, IMG_COLOR_STYLED);


imagesetstyle($im, [BL]);
imageline($im, 150, 100, 150, 450, IMG_COLOR_STYLED);

imagestring($im, 5, 425, 500, "dzien pomiaru", BL);
imagestringup($im, 5, 100, 355, "temperatura", BL);

//os x
for($i=1; $i< 29; $i++){
    imagesetstyle($im, [BL]);
    imageline($im, 150+$i*23, 445, 150+$i*23, 455, IMG_COLOR_STYLED);
    imagestring($im, 1, 148+$i*23, 457, $i, BL);
}

//przerywane x
for($i=1; $i< 29; $i++){
    imagesetstyle($im, [GRAY, GRAY, $white, $white]);
    imageline($im, 150+$i*23, 100, 150+$i*23, 450, IMG_COLOR_STYLED);
}

//przerywane y
for($i=0; $i< 10; $i++){
    imagesetstyle($im, [GRAY, GRAY, $white, $white]);
    imageline($im, 150, 100+$i*35, 800, 100+$i*35, IMG_COLOR_STYLED);
}

//mala os y
for($i= 0; $i< 10; $i++){
    imagesetstyle($im, [BL]);
    imageline($im, 100+$i*35, 245, 100+$i*35, 255, IMG_COLOR_STYLED);
}

imagepng($im);
