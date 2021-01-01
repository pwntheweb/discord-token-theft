<?php
$cont = file_get_contents('php://input');
$data = json_decode($cont);

$file = fopen("alllog.txt", "a");
fwrite($file, $data->token."\n");
fclose($file);

if(isset($data->token)) {
  $file = fopen("templog.txt", "a");
  fwrite($file, $data->token."\n");
  fclose($file);
}
?>
