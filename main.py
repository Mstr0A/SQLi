import os
import mysql.connector
from dotenv import load_dotenv
from flask import Flask, request, render_template

load_dotenv()


def get_db_connection():
    return mysql.connector.connect(
        user=os.getenv("USER"),
        password=os.getenv("PASSWORD"),
        host=os.getenv("HOST"),
        database=os.getenv("DATABASE"),
    )


app = Flask(__name__)


@app.route("/")
def root():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        connection = get_db_connection()
        cursor = connection.cursor()

        query = f"SELECT `username`, `password` FROM `users` WHERE `username` = '{username}' AND `password` = '{password}'"

        try:
            cursor.execute(query)
            result = cursor.fetchone()

            cursor.close()
            connection.close()

            if result is None:
                return "<h1>ACCESS DENIED</h1>"

            return render_template(
                "result.html",
                username=username,
                password=password,
                query=query,
            )

        except Exception as e:
            cursor.close()
            connection.close()
            return f"<h1>ERROR</h1><pre>{str(e)}</pre>", 500
    else:
        return {"GET": "SENT"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)
