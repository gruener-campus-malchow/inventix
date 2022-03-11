<!DOCTYPE html>
<html lang="de">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Titel</title>
  </head>
  <body>
  <?php
    require 'lib\phpqrcode-2010100721_1.1.4\phpqrcode\qrlib.php';

    $relativePathForDumping = 'QrCodes\\';
    $url = 'String goes here (url still kinda buggi)';

    QRcode::png($url, $relativePathForLib.$url.'.png');
    echo '<img src="'.$relativePathForLib.$url.'.png"/>';
    echo 'Hier is nen tolles bild';
    
    //phpinfo();
    ?>
  </body>
</html>

