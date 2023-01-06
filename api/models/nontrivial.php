<?php

class nontrivial extends Model
{
	protected $name = 'nontrivial';
    protected $id = 'id';
    protected $searchable = ['firstname', 'lastname', 'username', 'email'];
    protected $insertable = ['firstname', 'lastname', 'username', 'email', 'passwort_hash'];
    
    public function getAll($filter){
        
        $query='SELECT "THIS IS A NONTRIVIAL REQUEST"';
        $params = [];
        $this->api_response($this->db->query($query, $params));
    }


    //$body = json_decode(file_get_contents('php://input'), true);
}
