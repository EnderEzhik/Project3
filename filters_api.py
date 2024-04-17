import flask

from flask import render_template, redirect
from db_manage import *


blueprint = flask.Blueprint("filters_api", __name__, template_folder="templates")


@blueprint.route("/filters")
def filters():
    return render_template("filters.html")


@blueprint.route("/black-list")
def black_list():
    return render_template("filter_list.html", content=get_black_list(), type_list="black")


@blueprint.route("/white-list")
def white_list():
    return render_template("filter_list.html", content=get_white_list(), type_list="white")


@blueprint.route("/add-black-list")
def add_black_list_menu():
    accounts = list()
    for account in get_accounts():
        if exist_in_black_list(account.user_id) == False and exist_in_white_list(account.user_id) == False:
            accounts.append(account)
    
    return render_template("users.html", accounts=accounts, type_list="black")


@blueprint.route("/add-black-list/<user_id>")
def add_black_list(user_id):
    add_to_black_list(user_id)
    return redirect("/add-black-list")


@blueprint.route("/delete-black-list/<int:user_id>")
def delete_user_form_black_list(user_id):
    remove_from_black_list(user_id)
    return redirect("/black-list")


@blueprint.route("/add-white-list")
def add_white_list_menu():
    accounts = list()
    for account in get_accounts():
        if exist_in_black_list(account.user_id) == False and exist_in_white_list(account.user_id) == False:
            accounts.append(account)
    
    return render_template("users.html", accounts=accounts, type_list="white")


@blueprint.route("/add-white-list/<user_id>")
def add_white_list(user_id):
    add_to_white_list(user_id)
    return redirect("/add-white-list")


@blueprint.route("/delete-white-list/<int:user_id>")
def delete_user_form_white_list(user_id):
    remove_from_white_list(user_id)
    return redirect("/white-list")