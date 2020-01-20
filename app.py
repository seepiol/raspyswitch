from flask import Flask, request, redirect
import subprocess
import RPi.GPIO as GPIO
import time
import sqlite3

app = Flask(__name__)

conn = sqlite3.connect("actions.db", check_same_thread=False)

try:
    conn.execute(
        """CREATE TABLE SWITCHCRON
                (ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                ACTION   TEXT    NOT NULL,
                DATETIME  TEXT    NOT NULL
                );"""
    )
except:
    pass


@app.route("/")
@app.route("/home")
def home():
    return """
        <h1>RASPYSWITCH</h1>
        <a href="/light?to=on">ON</a>
        <a href="/light?to=off">OFF</a>
            """


@app.route("/light")
def light():
    switch = request.args.get("to")
    print(subprocess.call("pwd"))
    if switch == "on":
        actiontime = time.asctime(time.localtime(time.time()))
        subprocess.call(["python3", "./on.py"])
        conn.execute(
            f'INSERT INTO SWITCHCRON (ACTION, DATETIME)VALUES ("ON", "{actiontime}");'
        )
        conn.commit()

    elif switch == "off":
        subprocess.call(["python3", "./off.py"])
        actiontime = time.asctime(time.localtime(time.time()))
        conn.execute(
            f'INSERT INTO SWITCHCRON (ACTION, DATETIME)VALUES ("OFF", "{actiontime}");'
        )
        conn.commit()

    return redirect("/home")


if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=4000)
