DROP TABLE songs;

CREATE TABLE songs(
    ID INTEGER PRIMARY KEY,
    Title TEXT,
    Artist TEXT,
    Album TEXT,
    Genre TEXT,
    Duration TEXT
)


INSERT INTO songs("ID", "Title", "Artist", "Album", "Genre", "Duration")
VALUES(1, "Song 2", "Artist 1", "Album 1", "Pop", 200)

INSERT INTO songs("ID", "Title", "Artist", "Album", "Genre", "Duration")
VALUES(2, "Song 2", "Artist 2", "Album 2", "Rock", 300)

INSERT INTO songs("ID", "Title", "Artist", "Album", "Genre", "Duration")
VALUES(3, "Song 3", "Artist 3", "Album 3", "Hip Hop", 250)

INSERT INTO songs("ID", "Title", "Artist", "Album", "Genre", "Duration")
VALUES(4, "Song 4", "Artist 4", "Album 4", "Electronic", 180)

INSERT INTO songs("ID", "Title", "Artist", "Album", "Genre", "Duration")
VALUES(5, "Song 5", "Artist 5", "Album 5", "R&B", 320)

UPDATE songs
SET title = 'New Title'
WHERE ID = 1;