<?php

class descriptions extends Model
{
	protected $name = 'description';
    protected $id = 'id';
    protected $searchable = ['id', 'status'];
    protected $insertable = ['text', 'status'];
}