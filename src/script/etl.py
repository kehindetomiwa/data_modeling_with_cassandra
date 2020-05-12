import pandas as pd
from cassandra.cluster import Cluster
from file_loader import process_files
from queries import *

try:
    cluster = Cluster()
    session = cluster.connect()
except Exception as e:
    print(e)


def create_or_drop_table(query):
    try:
        session.execute(query)
    except Exception as e:
        print(e)


def select_rows(query):
    try:
        rows = session.execute(query)
    except Exception as e:
        print(e)

    for row in rows:
        print(list(row))


def main():
    path = '/../../event_data/'

    process_files(path)
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

    create_or_drop_table(music_history_table)

    for i, row in df.iterrows():
        query = "INSERT INTO music_history (session_id, itemInSession, artist, song, length)"
        query += "VALUES(%s, %s, %s, %s, %s)"
        session.execute(query, (row.sessionId, row.itemInSession, row.artist, row.song, row.length))

    select_rows(music_history_select)

    create_or_drop_table(user_history_table)

    for i, row in df.iterrows():
        query = "INSERT INTO user_history (user_id, sessionId, itemInSession, artist, song, firstName, lastName)"
        query += "VALUES(%s, %s, %s, %s, %s, %s, %s)"
        session.execute(query, (
        row.userId, row.sessionId, row.itemInSession, row.artist, row.song, row.firstName, row.lastName))

    select_rows(user_history_select)

    create_or_drop_table(song_history_table)

    for i, row in df.iterrows():
        query = "INSERT INTO song_history (song, userId, firstName, lastName)"
        query += "VALUES(%s, %s, %s, %s)"
        session.execute(query, (row.song, row.userId, row.firstName, row.lastName))

    select_rows(song_history_select)




if __name__ == '__main__':
    main()