from flask import Flask
import sqlite3

app = Flask("my flask app")
conn = sqlite3.connect("users.db", check_same_thread=False)

conn.execute("CREATE TABLE IF NOT EXISTS users (user_id int);")
conn.commit()


@app.post("/user")
def create_user():
    conn.execute("INSERT INTO users VALUES (1)")
    conn.commit()
    print("Пользователь создан")
    return"Пользователь создан"


@app.get("/user")
def get_user():
    print("Пользователь получен")
    return [row for row in conn.execute("SELECT * from users;")]


@app.delete("/user")
def delete_user():
    print("Пользователь удален")
    return "Пользователь удален"


@app.patch("/user")
def patch_user():
    print("Пользователь обновлён")
    return "Пользователь обновлён"


app.run()
