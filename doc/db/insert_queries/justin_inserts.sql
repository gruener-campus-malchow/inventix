INSERT INTO locations (house, room, specification) 
VALUES 
('FGIII', '207', 'erster Schrank neben Tür, oberes Fach');

INSERT INTO role (id, name, create, write, read)
VALUES (6, GeWi-Lehrer, FALSE, FALSE, TRUE);

INSERT INTO categories (id, name) VALUES (10, 'FB_GeWi');

INSERT INTO read_categories (role_id_fk, categories_id_fk) VALUES (6, 10);

INSERT INTO user (id, firstname, lastname, username, email, passwort_hash)
VALUES (9, Henry, Henrisson, HHson, Henry@easymail.org, FTFZJKSDF784FTRJIDF2GFZXDHZISDFASDDGUIOPGHJK);

INSERT INTO assigned_role (user_id_fk, role_id_fk) VALUES (9, 6);

