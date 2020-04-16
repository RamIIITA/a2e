
################# POSTGRES ############
sql type -> psql

TEXT ->  Text data of unlimited character
TEXT [] -> Array

we can create a table with image field by using types as oid or bytea
if we are using bytea while inserting we have to use values(bytea('image location'))  ###### It converts the string constant to its binay representation
                                                     values(lo_import('image location'))    directly stores the image

                or 
we can upload a image by decoding it to hexastring  to bytes and store in bytea datatype column in postgres
for that

values (decode('HexStringOfImage', hex));


################### CREATE TABLE (called events)##############

CREATE TABLE events(
                        event_id serial PRIMARY KEY,
                        creater_id INTEGER NOT NULL,
                        participents TEXT[],
                        teams TEXT[] NOT NULL,
                        title  TEXT NOT NULL UNIQUE,
                        keywords TEXT[] , 
                        description TEXT NOT NULL, 
                        prequisites TEXT , 
                        doc bytea,
                        ppt bytea,
                        image bytea, 
                        approved BOOLEAN DEFAULT FALSE, 
                        summary  TEXT, 
                        created_date TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT now(),
                        event_date TIMESTAMP WITH TIME ZONE NOT NULL,
                        updated_date TIMESTAMP,
                        cancel  BOOLEAN DEFAULT FALSE,
                    );


######################## Create Event #################################
Get the user id from the session

INSERT
INTO events
(creater_id, teams, title, keywords, description, prequisites, doc, ppt, image, event_date)
VALUES
(
    "1", ARRAY['front end', 'backend'], "Title One", ARRAY['Webdev', 'OAuth'] ,"This is description", "enter the prequisites", pg_read_binary_file('path/doc'), pg_read_binary_file('path/ppt'),
    pg_read_binary_file('path/image'),  '2020-04-20 10:26:41-01'

);


######################## update events ####################################
First get the user ID from Session and compare the session ID with updating row creater ID while updating


UPDATE events
SET updated_date = '2021-04-20 10:26:41-01'
WHERE 
    (event_id = '1' AND creater_id= '1')



####################### Search by table using Arrays  data#######################

SELECT * FROM events WHERE "web" = ANY(keywords);

SELECT * FROM events WHERE Array["web", "OAUTH"] = ALL(keywords);

