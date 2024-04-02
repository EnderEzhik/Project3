import flask
import db_manage
import json
import os

from flask import render_template, redirect


blueprint = flask.Blueprint("chats_api", __name__, template_folder="templates")


@blueprint.route("/chat")
def all_chats():
    chats = db_manage.get_accounts()
    return render_template("chats.html", chats=chats)


@blueprint.route("/chat/<chat_id>")
def one_chat(chat_id):
    chat = db_manage.get_account(chat_id)
    if os.path.exists(f"data\\chats\\{chat_id}\\messages.json"):
        with open(f"data\\chats\\{chat_id}\\messages.json", "r", encoding="UTF-8") as file:
            messages = json.load(file)
    else:
        messages = []
    return render_template("chat.html", chat=chat, messages=messages)
