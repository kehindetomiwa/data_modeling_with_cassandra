import pandas as pd
from cassandra.cluster import Cluster
from file_loader import process_files
from queries import *



def main():
    path = '/../../event_data/'
    #create the small file
    process_files(path)

    try:
        cluster = Cluster()
        session = cluster.connect()
    except Exception as e:
        print(e)

    try:
        session.execute(create_keyspace_music_db)
    except Exception as e:
        print(e)

    try:
        session.set_keyspace('music_db')
    except Exception as e:
        print(e)

    df = pd.read_csv('event_datafile_new.csv', encoding='utf8')
    print(df.head())

    try:
        session.execute(music_history_table)
    except Exception as e:
        print(e)

    for i, row in df.iterrows():
        session.execute(music_history_insert, (row.sessionId,
                                               row.itemInSession,
                                               row.artist, row.song,
                                               row.length))
    try:
        rows = session.execute(music_history_select)
    except Exception as e:
        print(e)

    for row in rows:
        print(row)


    try:
        session.execute(user_history_table)
    except Exception as e:
        print(e)

    for i, row in df.iterrows():
        session.execute(user_history_insert, (row.userId,
                                row.sessionId,
                                row.itemInSession,
                                row.artist, row.song,
                                f'{row.firstName} {row.lastName}'))

    try:
        rows = session.execute(user_history_select)
    except Exception as e:
        print(e)

    for row in rows:
        print(row)


    try:
        session.execute(song_history_table)
    except Exception as e:
        print(e)

    for i, row in df.iterrows():
        session.execute(song_history_insert, (row.song, f'{row.firstName} {row.lastName}'))
    try:
        rows = session.execute(song_history_select)
    except Exception as e:
        print(e)

    for row in rows:
        print(row)




if __name__ == '__main__':
    main()