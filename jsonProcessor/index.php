<?php

$json = json_decode(file_get_contents('../word.json'), true);

$distanceList = [];
$returnList = [];
foreach ($json as $key => $item) {
    $json[$key]['distance'] = $distanceList[] = sqrt(pow($item['x'] - 0, 2) + pow($item['y'] - 0, 2));
}

foreach ($json as $key => $item) {
    if($item['distance'] < 10) {
        $returnList[] = $item;
    }
}

$file = fopen('./word.json', 'w+b');
fwrite($file, json_encode($returnList));
fclose($file);