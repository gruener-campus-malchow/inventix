<?php

class items extends Model
{
	protected $name = 'items';
    protected $id = 'id';
	protected $searchable = ['name'];
	protected $insertable = ['name'];
}