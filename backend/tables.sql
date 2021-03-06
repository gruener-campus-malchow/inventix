PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS Nutzer(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    vorname TEXT,
    nachname TEXT,
    mail TEXT,
	pwhash TEXT
);

CREATE TABLE IF NOT EXISTS Fachbereiche(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    longname TEXT,
    shortname TEXT
);

CREATE TABLE IF NOT EXISTS FachbereichNutzer(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Nutzer_id INTEGER,
    Fachbereich_id INTEGER
);

CREATE TABLE IF NOT EXISTS Items(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    notiz TEXT,
	visible_with_no_login BOOL,
	Position_id INTEGER,
	Nutzer_id INTEGER,
	Fotos_id INTEGER
);

CREATE TABLE IF NOT EXISTS Fotos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    uri TEXT
);

CREATE TABLE IF NOT EXISTS FachbereichItem(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Items_id INTEGER,
    Fachbereich_id INTEGER
);

CREATE TABLE IF NOT EXISTS Tags(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tag TEXT
);

CREATE TABLE IF NOT EXISTS TagItem(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Items_id INTEGER,
    Tags_id INTEGER
);

CREATE TABLE IF NOT EXISTS Position(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Ort_id INTEGER,
    Raum_id INTEGER,
	kurzbezeichnung TEXT
);

CREATE TABLE IF NOT EXISTS Ort(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT
);

CREATE TABLE IF NOT EXISTS Raum(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT
);








