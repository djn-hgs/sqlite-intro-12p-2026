import sqlite3 as sql

conn = sql.connect("chinook.db")

cursor = conn.cursor()

artist_search = input("Enter the artist name: ")

artists_query = """
SELECT Name
FROM artists
WHERE Name ;
"""

cursor.execute(artists_query, (artist_search,))

print(cursor.fetchone())
# print(cursor.fetchone())
# print(cursor.fetchmany(5))
#
# as_a_list = cursor.fetchmany(10)
#
# print(as_a_list)
#
# magic_query = """
# SELECT Title, artists.Name, tracks.Name
# FROM artists
# JOIN albums
# JOIN tracks
# WHERE albums.ArtistId=artists.ArtistId
# AND tracks.AlbumID=albums.AlbumID
# AND artists.Name='AC/DC'
# """
#
# cursor.execute(magic_query)
# print(cursor.fetchmany(10))


conn.close()
