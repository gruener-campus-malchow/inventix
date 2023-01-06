<?php

class categories extends Model
{
	protected $name = 'categories';
    protected $id = 'id';
    protected $searchable = ['id', 'name'];
    protected $insertable = ['name'];
}