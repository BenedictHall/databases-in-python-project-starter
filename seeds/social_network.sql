DROP TABLE IF EXISTS posts;
DROP SEQUENCE IF EXISTS posts_id_seq;
DROP TABLE IF EXISTS accounts cascade;
DROP SEQUENCE IF EXISTS accounts_id_seq;

CREATE SEQUENCE IF NOT EXISTS accounts_id_seq;
CREATE TABLE accounts (
    id SERIAL PRIMARY KEY,
    username VARCHAR(255),
    email VARCHAR(255)
);

CREATE SEQUENCE IF NOT EXISTS posts_id_seq;
CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    contents text,
    views int,
    account_id int,
    constraint fk_account foreign key(account_id)
    references accounts(id)
    on delete cascade
);

INSERT INTO accounts (username, email) VALUES ('Fake_guy_1', 'fake1@gmail.com');
INSERT INTO accounts (username, email) VALUES ('Fake_guy_2', 'fake2@gmail.com');
INSERT INTO posts (title, contents, views, account_id) VALUES ('new game', 'wow guys new game', 18, 1);
INSERT INTO posts (title, contents, views, account_id) VALUES ('new movie', 'wow guys new movie', 45, 1);
INSERT INTO posts (title, contents, views, account_id) VALUES ('new anime', 'wow guys new anime', 28, 2);
INSERT INTO posts (title, contents, views, account_id) VALUES ('new sport', 'wow guys new sport', 8, 2);