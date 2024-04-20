import flask

from flask import render_template, redirect, request


name = "menu_api"
template_folder = "templates"

blueprint = flask.Blueprint(name, __name__, template_folder=template_folder)


@blueprint.route("/menu")
def menu():
    cookie = request.cookies.get("login")
    
    if cookie == "true":
        pass
    elif cookie == "None":
        return redirect("/login")
    else:
        return redirect("/register")
    
    return render_template("menu.html")
