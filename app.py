from flask import Flask, request, redirect
import subprocess
import RPi.GPIO as GPIO
import time


app=Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return '''
        <h1>RASPYSWITCH</h1>
        <a href="/light?to=on">ON</a>
        <a href="/light?to=off">OFF</a>
            '''

@app.route("/light")
def light():
    switch = request.args.get("to")
    print(subprocess.call("pwd"))
    if switch ==  "on":
        subprocess.call(["python3", "./on.py"])

    elif switch == "off":
        subprocess.call(["python3", "./off.py"])

    return redirect("/home")

if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=4000)
