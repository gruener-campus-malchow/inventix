PRAGMA foreign_keys = ON;

CREATE TABLE fachbereich (
    id INT PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    alt TEXT,
    abkuerzung TEXT
);

CREATE TABLE nutzer (
    id INT PRIMARY KEY AUTOINCREMENT,
    nickname TEXT UNIQUE,
    vorname TEXT,
    nachname TEXT,
    email TEXT,
    password TEXT,
    fachbereich_id INT,
    FOREIGN KEY (fachbereich_id) REFERENCES fachbereich(id)
);

CREATE TABLE foto (
    id INT PRIMARY KEY AUTOINCREMENT,
    uri TEXT,
    visible BOOL
);

CREATE TABLE datei (
    id INT PRIMARY KEY AUTOINCREMENT,
    uri TEXT,
    visible BOOL
);

CREATE TABLE tag (
    id INT PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    visible BOOL
);

CREATE TABLE gebaeude (
    id INT PRIMARY KEY AUTOINCREMENT,
    name TEXT
);

CREATE TABLE raum (
    id INT PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    gebaeude_id INT,
    FOREIGN KEY (gebaeude_id) REFERENCES gebaeude(id)
);

CREATE TABLE moebel (
    id INT PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    raum_id INT,
    FOREIGN KEY (raum_id) REFERENCES raum(id)
);

CREATE TABLE ort (
    id INT PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    moebel_id INT,
    FOREIGN KEY (moebel_id) REFERENCES moebel(id)
);

CREATE TABLE gegenstand (
    id INT PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    notes TEXT,
    foto_id INT,
    ort_id INT,
    nutzer_id INT,
    visible BOOL,
    FOREIGN KEY (foto_id) REFERENCES foto(id),
    FOREIGN KEY (ort_id) REFERENCES ort(id),
    FOREIGN KEY (nutzer_id) REFERENCES nutzer(id)
);

CREATE TABLE datei_gegenstand (
    datei_id INT,
    gegenstand_id INT,
    FOREIGN KEY (datei_id) REFERENCES datei(id),
    FOREIGN KEY (gegenstand_id) REFERENCES gegenstand(id)
)