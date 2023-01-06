<?php

class tags extends Model
{
	protected $name = 'tags';
    protected $id = 'id';
    protected $searchable = ['label', 'status'];
	protected $insertable = ['label', 'status'];
}