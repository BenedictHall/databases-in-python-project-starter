-- The job of this file is to reset the tables and add data for tests to run

--First drop all our tables
DROP TABLE IF EXISTS recipes;
DROP SEQUENCE IF EXISTS recipes_id_seq;

-- Then recreate the table
CREATE SEQUENCE IF NOT EXISTS recipes_id_seq;
CREATE TABLE recipes(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    cooking_time int,
    rating int
);

--Finally add records needed for the tests to run
INSERT INTO recipes (name, cooking_time, rating) VALUES ('Meatloaf', 60, 1);
INSERT INTO recipes (name, cooking_time, rating) VALUES ('Spaghetti', 20, 4);
INSERT INTO recipes (name, cooking_time, rating) VALUES ('Sandwich', 5, 3);
INSERT INTO recipes (name, cooking_time, rating) VALUES ('Lasagna', 120, 5);
