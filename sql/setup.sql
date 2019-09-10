PRAGMA foreign_keys = ON;

CREATE TABLE fachbereich (
    id PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    alt TEXT,
    abkuerzung TEXT
)

CREATE TABLE nutzer (
    id PRIMARY KEY AUTOINCREMENT,
    nickname TEXT UNIQUE,
    vorname TEXT,
    nachname TEXT,
    email TEXT,
    password TEXT,
    fachbereich_id INT,
    FOREIGN KEY fachbereich_id REFERENCES fachbereich(id)
)

CREATE TABLE foto (
    id PRIMARY KEY AUTOINCREMENT,
    uri TEXT,
    visible BOOL
)