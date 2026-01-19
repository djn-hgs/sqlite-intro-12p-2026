import sqlite3

connection = sqlite3.connect("social_media_db.db")

cursor = connection.cursor()

create_user_sql = """
CREATE TABLE IF NOT EXISTS user (
id INTEGER PRIMARY KEY AUTOINCREMENT,
username TEXT
);
"""

cursor.execute(create_user_sql)

create_post_sql = """
CREATE TABLE IF NOT EXISTS post (
id INTEGER PRIMARY KEY AUTOINCREMENT,
user_id INTEGER,
post_text TEXT
);
"""

cursor.execute(create_post_sql)

connection.commit()

insert_user_sql = """
INSERT INTO
    user (username)
VALUES
    (?)
;
"""

insert_post_sql = """
                  INSERT INTO post (user_id, post_text)
                  VALUES (?, ?)
                  ; \
                  """

query_user_sql = """
            SELECT *
            FROM user;
            """

query_specific_user_sql = """
            SELECT id, username
            FROM user
            WHERE username IS ?;
                """

query_post_sql = """
            SELECT username, post_text
            FROM post
            INNER JOIN user
            ON post.user_id = user.id
            ;
                """

query_users_posts = """
            SELECT post_text
            FROM post
            INNER JOIN user
            ON post.user_id = user.id
            WHERE user.id=?
            ;
                    """

delete_user_sql = """
            DELETE
            FROM user
            WHERE username = (?);
             """

logged_in_userid = None
logged_in_username = None

while True:
    print(f"Logged in as {logged_in_username}")
    print("0: Quit")
    print("1: Add user")
    print("2: List users")
    print("3: Delete user")
    print("4: Log in")
    print("5: Post")
    print("6: Show all posts")
    print("7: Show your posts")

    choice = int(input("Enter your choice: "))

    if choice == 0:
        break

    elif choice == 1:
        username = input("Enter new username: ")
        cursor.execute(insert_user_sql, (username,))

    elif choice == 2:
        user_query = cursor.execute(query_user_sql).fetchall()
        print(user_query)

    elif choice == 3:
        username = input("Enter username to delete: ")
        delete_user = cursor.execute(delete_user_sql, (username,))

    elif choice == 4:
        username = input("Enter your username: ")
        user_query = cursor.execute(query_specific_user_sql, (username,))
        user_query_response = user_query.fetchone()

        if user_query_response:
            logged_in_userid, logged_in_username = user_query_response
            print(f"Logged in as {logged_in_username}")
        else:
            logged_in_userid = None
            logged_in_username = None

    elif choice == 5:
        if logged_in_userid:
            post_text = input(f"What is your post, {logged_in_username}?")
            cursor.execute(insert_post_sql, (logged_in_userid, post_text))
            connection.commit()

        else:
            print("No one is logged in")

    elif choice == 6:
        cursor.execute(query_post_sql)
        post_query = cursor.fetchall()

        for username, post_text in post_query:
            print(f"{username}: {post_text}")

    elif choice == 7:
        cursor.execute(query_users_posts, (logged_in_userid,))
        user_post_query = cursor.fetchall()

        for post_text in user_post_query:
            print(post_text)

    connection.commit()

connection.commit()
connection.close()

