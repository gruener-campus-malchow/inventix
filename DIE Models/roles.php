<?php

class roles extends Model
{
	protected $name = 'role';
    protected $id = 'id';
    protected $searchable = ['id', 'name', 'create', 'write', 'read'];
    protected $insertable = [];
}