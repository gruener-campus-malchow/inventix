<?php
require_once('model.php');
class jokes extends model{

	public function readAll()
	{
		// öffnen des Verzeichnisses
		$dir = '../humor/';
		if ( $handle = opendir($dir) )
		{
			// einlesen der Verzeichnisses
			$data = array();
			//array_push($data, 'put some files into list');
			while (($file = readdir($handle)) !== false)
			{
				
				
				if (array_pop(explode('.',$file))== 'md')
				{
					$joke = array();
					$joke['filename'] = $file;
					$jokefile = fopen($dir.$file, "r");
					$joke['joke'] = fread($jokefile,filesize($dir.$file));
					array_push($data, $joke);
					fclose($jokefile);
				}

					
					
				
				
			}
			closedir($handle);
		}else{
			array_push($this->debugMessages, 'not a working directory');
			array_push($data, 'not a working directory');
		}
		return $data;
		
		
	}
	
}
?>
