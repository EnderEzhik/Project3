import flask

from flask import render_template, redirect, request
from db_manage import *

name = "filters_api"
template_folder = "templates"

blueprint = flask.Blueprint(name, __name__, template_folder=template_folder)


@blueprint.route("/filters")
def filters():
    cookie = request.cookies.get("login")
    
    if cookie == "true":
        pass
    elif cookie == "None":
        return redirect("/login")
    else:
        return redirect("/register")
    
    return render_template("filters.html")


@blueprint.route("/black-list")
def black_list():
    cookie = request.cookies.get("login")

    if cookie == "true":
        pass
    elif cookie == "None":
        return redirect("/login")
    else:
        return redirect("/register")
    
    content = get_black_list()
    type_list = "black"
    
    return render_template("filter_list.html", content=content, type_list=type_list)


@blueprint.route("/white-list")
def white_list():
    cookie = request.cookies.get("login")
    
    if cookie == "true":
        pass
    elif cookie == "None":
        return redirect("/login")
    else:
        return redirect("/register")
    
    content = get_white_list()
    type_list = "white"

    return render_template("filter_list.html", content=content, type_list=type_list)


@blueprint.route("/add-black-list")
def add_black_list_menu():
    cookie = request.cookies.get("login")

    if cookie == "true":
        pass
    elif cookie == "None":
        return redirect("/login")
    else:
        return redirect("/register")
    
    type_list = "black"
    accounts = list()

    for account in get_accounts():
        user_id = account.user_id
        if exist_in_black_list(user_id) == False:
            if exist_in_white_list(user_id) == False:
                accounts.append(account)
    
    return render_template("users.html", accounts=accounts, type_list=type_list)


@blueprint.route("/add-black-list/<user_id>")
def add_black_list(user_id):
    cookie = request.cookies.get("login")

    if cookie == "true":
        pass
    elif cookie == "None":
        return redirect("/login")
    else:
        return redirect("/register")
    
    add_to_black_list(user_id)

    return redirect("/add-black-list")


@blueprint.route("/delete-black-list/<int:user_id>")
def delete_user_form_black_list(user_id):
    cookie = request.cookies.get("login")

    if cookie == "true":
        pass
    elif cookie == "None":
        return redirect("/login")
    else:
        return redirect("/register")
    
    remove_from_black_list(user_id)

    return redirect("/black-list")


@blueprint.route("/add-white-list")
def add_white_list_menu():
    cookie = request.cookies.get("login")

    if cookie == "true":
        pass
    elif cookie == "None":
        return redirect("/login")
    else:
        return redirect("/register")
    
    type_list = "white"
    accounts = list()

    for account in get_accounts():
        user_id = account.user_id
        if exist_in_black_list(user_id) == False:
            if exist_in_white_list(user_id) == False:
                accounts.append(account)
    
    return render_template("users.html", accounts=accounts, type_list=type_list)


@blueprint.route("/add-white-list/<user_id>")
def add_white_list(user_id):
    cookie = request.cookies.get("login")

    if cookie == "true":
        pass
    elif cookie == "None":
        return redirect("/login")
    else:
        return redirect("/register")

    add_to_white_list(user_id)

    return redirect("/add-white-list")


@blueprint.route("/delete-white-list/<int:user_id>")
def delete_user_form_white_list(user_id):
    cookie = request.cookies.get("login")

    if cookie == "true":
        pass
    elif cookie == "None":
        return redirect("/login")
    else:
        return redirect("/register")

    remove_from_white_list(user_id)

    return redirect("/white-list")