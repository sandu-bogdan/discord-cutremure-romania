<?php 
$lastNearthquake = htmlspecialchars($_GET["last"]);
$type = htmlspecialchars($_GET["type"]);

$opts = array('http' =>
    array(
        'method'  => 'GET',
    ),
    "ssl"=>array(
      "verify_peer"=>false,
      "verify_peer_name"=>false,
  )
);
$context  = stream_context_create($opts);

//get contents from a infp.ro
$getInfp = file_get_contents("https://web.infp.ro/quakes?includemagnitudes=any&page=0", false, $context);
$jsonDecode = json_decode($getInfp, true);
$result = $jsonDecode['result'];
$earthquakeArray=array();

foreach($result as $results) {
  if($results['sols']['primary']['region']['type'] == 'local'){
    array_push($earthquakeArray, str_replace('T',' ',$results['sols']['primary']['time']).','.$results['sols']['primary']['magnitudes']['ml']['value'].','.$results['sols']['primary']['region']['name']);
  }
}

if($lastNearthquake != 0){
  for($i=0;$i<$lastNearthquake;$i++){
    echo $earthquakeArray[$i].';';
  }
}
else
    if($type == 'ews'){
        $getInfpEws = file_get_contents("http://ews.infp.ro/ajax.php?actiune=generare_tabel", false, $context);
        $jsonDecodeEws = json_decode($getInfpEws, true);
        $resultEws = $jsonDecodeEws['data'];
        echo $jsonDecodeEws['data'][0]['mag'],',',$jsonDecodeEws['data'][0]['data_eveniment'],',',$jsonDecodeEws['data'][0]['secundeS'],',',$jsonDecodeEws['data'][0]['lat'],',',$jsonDecodeEws['data'][0]['lng'];
    }
else
    if($type == 'recent')
        echo '2023-02-14 11:50:23.576,1.8,Transilvania. Covasna';
?>