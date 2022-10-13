<?php
require_once('model.php');
class jokes extends model{
	
	private $dir = '../humor/';

	public function readAll()
	{
		// öffnen des Verzeichnisses
		
		if ( $handle = opendir($this->dir) )
		{
			// einlesen der Verzeichnisses
			$data = array();
			//array_push($data, 'put some files into list');
			while (($file = readdir($handle)) !== false)
			{
				if (substr($file, -3) == '.md')
				{
					array_push($data, [
						'id' => $file,
						'joke' => file_get_contents($this->dir.$file)
					]);
				}
			}
			closedir($handle);
		}else{
			array_push($this->debugMessages, 'not a working directory');
			array_push($data, 'not a working directory');
		}
		return $data;
	}
	
	
	public function readSingle($id)
	{
		$data = array();
		if (file_exists($this->dir.$id) and substr($id, -3) == '.md')
		{
			array_push($data, [
				'id' => $id,
				'joke' => file_get_contents($this->dir.$id)
			]);
			
		}
		else
		{
			array_push($data, [
				'error' => 'not a valid id'
			]);
		}
		
		
		return $data;
	}

	public function getSpecial()
	{
		//this method have to be implemented in special model
		$data = array('You want special things, I cannot serve right now.');
		return $data;
	}


	public function update($id)
	{
		//this method have to be implemented with special model
		return TRUE;
	}
	
	public function delete($id)
	{
		
		$query = "DELETE FROM ".$id." WHERE id = :id;";
		
		$statement = $this->db->prepare($query);
		$statement->bindParam(':id', $id);
        $statement->execute();
        $data = $statement->fetchAll(PDO::FETCH_ASSOC);
		$this->addDebugMessages($statement);
		return $data;
	}
	public function create()
	{
		return array("this method have to be implemented with special model");
		
	}
	
	public function postSpecial()
	{
		return array("this method have to be implemented with special model");
		
	}
	
}
?>
