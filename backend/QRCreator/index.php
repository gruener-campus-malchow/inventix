<!DOCTYPE html>
<html lang="de">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Titel</title>
  </head>
  <body>

	<form method=get>
	<input type=input name=qrtext value="input text for QRC here">
	<input type=submit name=submit value=submit>
	</form>

  <?php
	if (isset($_GET['qrtext']))
	{
		require 'lib/phpqrcode-2010100721_1.1.4/phpqrcode/qrlib.php';

		$relativePathForDumping = 'QrCodes\\';
		$url = $_GET['qrtext'];

		$temp = 'qrcodes_'.random_int(1,1000000);
		QRcode::png($url, $relativePathForLib.$temp.'.png');
		echo '<img src="'.$relativePathForLib.$temp.'.png"/>';
		echo 'Hier is nen tolles bild';
    }
    //phpinfo();
    ?>
  </body>
</html>

