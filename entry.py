import json

from apis import filters_api
from apis import chats_api
from apis import menu_api
from apis import accounts_api
from data.Models.Register import RegisterForm
from data.Models.Login import LoginForm
from db_manage import *
from flask import Flask, render_template, redirect, make_response, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
app.config["SECRET_KEY"] = "123"
ip = "127.0.0.1"
port = 8080


def registration(username, password):
    with open("user.json", "w") as file:
        data = dict()
        data["username"] = username
        data["hash_password"] = generate_password_hash(password)
        json.dump(data, file)
    return


def check_password(password):
    with open("user.json") as file:
        hashed_password = json.load(file)["hash_password"]
    return check_password_hash(hashed_password, password)


@app.errorhandler(404)
def not_found(_):
    return make_response(jsonify({"error": "Not found"}), 404)


@app.errorhandler(400)
def bad_request(_):
    return make_response(jsonify({"error": "Bad Request"}), 400)


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template("registration.html",
                                   form=form,
                                   message="Пароли не совпадают")
        registration(form.username.data, form.password.data)
        response = make_response(redirect("/login"))
        response.set_cookie("login", "None")
        return response
    return render_template("registration.html", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if not check_password(form.password.data):
            return render_template("login.html",
                                   form=form,
                                   message="Неверный пароль")
        response = make_response(redirect("/menu"))
        response.set_cookie("login", "true")
        return response
    return render_template("login.html", form=form)


@app.route("/")
def entry():
    cookie = request.cookies.get("login")

    if cookie == "true":
        return redirect("/menu")
    if cookie == "None":
        return redirect("/login")
    
    return redirect("/register")


def main():
    app.register_blueprint(filters_api.blueprint)
    app.register_blueprint(chats_api.blueprint)
    app.register_blueprint(menu_api.blueprint)
    app.register_blueprint(accounts_api.blueprint)
    app.run(host=ip, port=port)
    return


if __name__ == "__main__":
    main()
