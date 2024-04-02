import filters_api, chats_api

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def menu():
    return render_template("menu.html")


def main():
    app.register_blueprint(filters_api.blueprint)
    app.register_blueprint(chats_api.blueprint)
    app.run(host="127.0.0.1", port=8080)

main()