create_keyspace_music_db =  ("""
                        CREATE KEYSPACE IF NOT EXISTS 
                            music_db
                        WITH REPLICATION =
                        { 'class' : 'SimpleStrategy', 'replication_factor' : 1 }
""")


music_history_table = "CREATE TABLE IF NOT EXISTS  \
                                music_history \
                    (session_id INT, \
                      session_item INT, \
                      artist TEXT, \
                      song TEXT, \
                      length FLOAT, \
                    PRIMARY KEY(session_id, session_item))"


music_history_insert = ("""INSERT INTO music_history 
                        (session_id, \
                        session_item, \
                        artist, \
                        song, \
                        length)
                        VALUES(%s, %s, %s, %s, %s)
""")

music_history_select = ("""
        SELECT 
        * 
        FROM 
        music_history 
        WHERE session_id=338 AND session_item=4
""")


user_history_table = "CREATE TABLE IF NOT EXISTS \
                        user_history \
                    (user_id INT, \
                    session_id INT, \
                    session_item INT, \
                    artist TEXT, \
                    song TEXT, \
                    user TEXT, \
                PRIMARY KEY((user_id), session_id, session_item))"

user_history_insert = (""" INSERT INTO user_history 
                        (user_id, \
                        session_id, \
                        session_item, \
                        artist, \
                        song, \
                        user) 
                        VALUES(%s, %s, %s, %s, %s, %s)
""")
user_history_select = ("""
            SELECT 
                * 
            FROM 
            user_history 
            WHERE user_id=10 AND session_id=182
""")


song_history_table = "CREATE TABLE IF NOT EXISTS song_history \
                    (song TEXT, \
                    user TEXT, \
                    PRIMARY KEY(song, user))"

song_history_insert = (""" INSERT INTO song_history 
                            (song, user) 
                        VALUES(%s, %s)
""")
song_history_select = ("""
            SELECT 
                * 
            FROM 
            song_history 
            WHERE song='All Hands Against His Own'
""")

