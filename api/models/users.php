<?php

class users extends Model
{
	protected $name = 'user';
    protected $id = 'id';
    protected $searchable = ['firstname', 'lastname', 'username', 'email'];
    protected $insertable = ['firstname', 'lastname', 'username', 'email', 'passwort_hash'];
}