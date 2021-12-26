DROP TABLE IF EXISTS person;
DROP TABLE IF EXISTS preference_types;
DROP TABLE IF EXISTS ingredient_types;
DROP TABLE IF EXISTS preference;

CREATE TABLE person (
    person_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL
);

CREATE TABLE preference_types (
    preference_type_id INTEGER PRIMARY KEY AUTOINCREMENT,
    description TEXT NOT NULL
);

CREATE TABLE ingredient_types (
    ingredient_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);

CREATE TABLE preference (
    preference_id INTEGER PRIMARY KEY AUTOINCREMENT,
	person_id INTEGER NOT NULL,
	ingredient_type_id INTEGER NOT NULL,
	preference_type_id INTEGER NOT NULL
);

INSERT INTO preference_types (preference_type_id, description)
VALUES (0, "Never tried, unsure");
VALUES (1, "Enjoy");
VALUES (2, "Will eat");
VALUES (3, "Will not eat");