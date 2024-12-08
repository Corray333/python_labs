-- +goose Up
CREATE TABLE artist (
    artist_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    genre TEXT NOT NULL,
    birth_date DATE NOT NULL
);

-- +goose Down
DROP TABLE artist;
