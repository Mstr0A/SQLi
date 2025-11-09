import mysql.connector


def get_db_connection():
    return mysql.connector.connect(
        user="user",
        password="password",
        host="host",
        database="database",
    )
