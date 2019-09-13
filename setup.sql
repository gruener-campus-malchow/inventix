PRAGMA foreign_keys = ON;

CREATE TABLE fachbereich (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    alt TEXT,
    abkuerzung TEXT
);

CREATE TABLE nutzer (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nickname TEXT UNIQUE,
    vorname TEXT,
    nachname TEXT,
    email TEXT,
    password TEXT,
    fachbereich_id INTEGER,
    FOREIGN KEY (fachbereich_id) REFERENCES fachbereich(id)
);

CREATE TABLE foto (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    uri TEXT,
    visible BOOL
);

CREATE TABLE datei (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    uri TEXT,
    visible BOOL
);

CREATE TABLE tag (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    visible BOOL
);

CREATE TABLE gebaeude (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT
);

CREATE TABLE raum (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    gebaeude_id INTEGER,
    FOREIGN KEY (gebaeude_id) REFERENCES gebaeude(id)
);

CREATE TABLE moebel (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    raum_id INTEGER,
    FOREIGN KEY (raum_id) REFERENCES raum(id)
);

CREATE TABLE ort (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    moebel_id INTEGER,
    FOREIGN KEY (moebel_id) REFERENCES moebel(id)
);

CREATE TABLE gegenstand (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    notes TEXT,
    foto_id INTEGER,
    ort_id INTEGER,
    nutzer_id INTEGER,
    visible BOOL,
    FOREIGN KEY (foto_id) REFERENCES foto(id),
    FOREIGN KEY (ort_id) REFERENCES ort(id),
    FOREIGN KEY (nutzer_id) REFERENCES nutzer(id)
);

CREATE TABLE datei_gegenstand (
    datei_id INTEGER,
    gegenstand_id INTEGER,
    FOREIGN KEY (datei_id) REFERENCES datei(id),
    FOREIGN KEY (gegenstand_id) REFERENCES gegenstand(id)
)