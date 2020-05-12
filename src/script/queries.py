create_keyspace_music_db =  ("""
                        CREATE KEYSPACE IF NOT EXISTS music_db
                        WITH REPLICATION =
                        { 'class' : 'SimpleStrategy', 'replication_factor' : 1 }""")


music_history_table = ("""
                CREATE TABLE IF NOT EXISTS music_history (
                session_id INT, 
                itemInSession INT, 
                artist TEXT, 
                song TEXT, 
                length FLOAT, 
                PRIMARY KEY(session_id, itemInSession)
                )""")


music_history_select = ("""SELECT 
                    artist, 
                    song, 
                    length 
                FROM music_history 
                WHERE session_id=338 AND itemInSession=4
                """)


user_history_table = ("""CREATE TABLE IF NOT EXISTS user_history(
                                user_id INT,
                                sessionId INT,
                                itemInSession INT,  
                                artist TEXT, 
                                song TEXT, 
                                firstName TEXT, 
                                lastName TEXT,
                       PRIMARY KEY(user_id, sessionId, itemInSession))""")


user_history_select = ("""SELECT 
                        itemInSession, 
                        artist, 
                        song, 
                        firstName,
                        lastName
                    FROM user_history 
                    WHERE user_id=10 AND sessionId=182""")


song_history_table = ("""CREATE TABLE IF NOT EXISTS song_history(
                        song TEXT, 
                        userId INT,
                        firstName TEXT, 
                        lastName TEXT,
               PRIMARY KEY(song, userId)
               )""")


song_history_select = ("""SELECT   userId,
                            firstName,
                            lastName
                    FROM song_history 
                    WHERE song='All Hands Against His Own'""")

