from db import get_db_connection
from flask import Flask, request, render_template


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
            print(e)
            exit(-1)
    else:
        return {"GET": "SENT"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)
