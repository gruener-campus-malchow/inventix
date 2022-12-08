BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS `user` (
	`id`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`firstname`	VARCHAR ( 255 ),
	`lastname`	VARCHAR ( 255 ),
	`username`	VARCHAR ( 255 ),
	`email`	VARCHAR ( 255 ),
	`passwort`	INTEGER
);
CREATE TABLE IF NOT EXISTS `tags` (
	`id`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`label`	VARCHAR ( 255 ),
	`status`	VARCHAR ( 255 ),
	`category_id_fk`	INTEGER,
	FOREIGN KEY(`category_id_fk`) REFERENCES `categories`(`id`)
);
CREATE TABLE IF NOT EXISTS `role` (
	`id`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`name`	VARCHAR ( 255 ),
	`create`	BOOLEAN,
	`read`	BOOLEAN,
	`write`	BOOLEAN
);
CREATE TABLE IF NOT EXISTS `locations` (
	`hause`	VARCHAR ( 255 ),
	`room`	VARCHAR ( 255 ),
	`specification`	VARCHAR ( 255 ),
	PRIMARY KEY(`hause`,`room`,`specification`)
);
CREATE TABLE IF NOT EXISTS `items` (
	`id`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`name`	VARCHAR ( 255 ),
	`location_hause_fk`	VARCHAR ( 255 ),
	`location_room_fk`	VARCHAR ( 255 ),
	`location_specification_fk`	VARCHAR ( 255 ),
	`description_id_fk`	INTEGER,
	FOREIGN KEY(`location_hause_fk`) REFERENCES `locations`(`hause`),
	FOREIGN KEY(`location_room_fk`) REFERENCES `locations`(`room`),
	FOREIGN KEY(`location_specification_fk`) REFERENCES `locations`(`specification`),
	FOREIGN KEY(`description_id_fk`) REFERENCES `description`(`id`)
);
CREATE TABLE IF NOT EXISTS `description` (
	`id`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`text`	TEXT,
	`status`	INTEGER ( 1 )
);
CREATE TABLE IF NOT EXISTS `category_access` (
	`category_id_fk`	INTEGER,
	`role_id_fk`	INTEGER,
	FOREIGN KEY(`category_id_fk`) REFERENCES `categories`(`id`),
	FOREIGN KEY(`role_id_fk`) REFERENCES `role`(`id`),
	PRIMARY KEY(`category_id_fk`,`role_id_fk`)
);
CREATE TABLE IF NOT EXISTS `categories` (
	`id`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`name`	VARCHAR ( 255 )
);
CREATE TABLE IF NOT EXISTS `assigned_role` (
	`user_id_fk`	INTEGER,
	`role_id_fk`	INTEGER,
	FOREIGN KEY(`user_id_fk`) REFERENCES `user`(`id`),
	PRIMARY KEY(`user_id_fk`,`role_id_fk`),
	FOREIGN KEY(`role_id_fk`) REFERENCES `role`(`id`)
);
COMMIT;
