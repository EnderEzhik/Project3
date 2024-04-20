import flask
import json
import os
import requests

from flask import render_template, redirect
from flask import request as flask_request


blueprint = flask.Blueprint("chats_api", __name__, template_folder="templates")


@blueprint.route("/chats")
def all_chats():
    cookie = flask_request.cookies.get("login")

    if cookie == "true":
        pass
    elif cookie == "None":
        return redirect("/login")
    else:
        return redirect("/register")
    
    chats = requests.get("http://127.0.0.1:8080/api/accounts").json()
    print(chats)

    return render_template("chats.html", chats=chats)


@blueprint.route("/chats/<user_id>")
def one_chat(user_id):
    cookie = flask_request.cookies.get("login")

    if cookie == "true":
        pass
    elif cookie == "None":
        return redirect("/login")
    else:
        return redirect("/register")
    
    user = requests.get(f"http://127.0.0.1:8080/api/accounts/{user_id}").json()

    if os.path.exists(f"data\\chats\\{user_id}\\messages.json"):
        with open(f"data\\chats\\{user_id}\\messages.json", "r", encoding="UTF-8") as file:
            messages = json.load(file)
    else:
        messages = []
    
    return render_template("chat.html", user=user, messages=messages)
