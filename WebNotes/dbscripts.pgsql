SET search_path TO webnotes;

DROP TABLE IF EXISTS notes;


CREATE TABLE IF NOT EXISTS notes(
    note_id varchar(64) NOT NULL PRIMARY KEY,
    title varchar(128) NOT NULL,
    date varchar(64) NOT NULL,
    text varchar(1024) NOT NULL,
    username varchar(128) NOT NULL,
    color varchar(8) NOT NULL
);

INSERT INTO notes VALUES(
    1, 'Note_1', '4-Feb-2021',
    'Hello World...! This is my first Note...',
    'abhishek', 'red'
);
INSERT INTO notes VALUES(
    2, 'Note_2', '5-Feb-2021',
    'This is my Second Note...',
    'abhishek', 'green'
);


INSERT INTO webnotes.notes VALUES(
    3, 'Note_3', '3-Feb-2021',
    'Third Note...',
    'abhi', 'blue'
);

INSERT INTO webnotes.notes VALUES(
    3, 'Note_3_2', '3-Feb-2021',
    'Third Note...',
    'abhi', 'blue'
);

UPDATE TABLE webnotes.notes SET


SELECT * FROM webnotes.notes;




SET search_path TO webnotes;
DELETE FROM webnotes.notes WHERE note_id='3';


SELECT * FROM notes WHERE username='abhishek';

SELECT * FROM webnotes.notes WHERE note_id='fb923b5b-d84d-4b6c-b156-d678dbc451eb';







SELECT random()::text;
SELECT md5(random()::text);



