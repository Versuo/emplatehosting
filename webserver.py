from flask import Flask
from threading import Thread

app = Flask('')
@app.route('/')
def home():
    return "Discord bot ok"


3 usages (2 dynamic)
def run():
    app.run(host="0.0.0.0", port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()
