<?php

$json = json_decode(file_get_contents('../word.json'), true);

$xList = [];
$yList = [];
$distanceList = [];
$returnList = [];
foreach ($json as $key => $item) {
    $xList[] = $item['x'];
    $yList[] = $item['y'];
    $json[$key]['distance'] = $distanceList[] = sqrt(pow($item['x'] - 0, 2) + pow($item['y'] - 0, 2));
}

var_dump(max($distanceList), min($distanceList));

foreach ($json as $key => $item) {
    if($item['distance'] < 10) {
        $returnList[] = $item;
    }
}

$file = fopen('./word.json', 'w+b');
fwrite($file, json_encode($returnList));
fclose($file);