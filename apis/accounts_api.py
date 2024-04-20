import flask
import db_manage

from flask import jsonify, make_response

name = "accounts_api"
template_folder = "templates"

blueprint = flask.Blueprint(name, __name__, template_folder=template_folder)


@blueprint.route("/api/accounts")
def get_all_accounts():
    accounts = db_manage.get_accounts()
    
    return jsonify(
        [item.to_dict(only=("user_id", "fname", "lname", "username", "names")) 
            for item in accounts]
    )


@blueprint.route("/api/accounts/<int:user_id>")
def get_one_account(user_id):
    account = db_manage.get_account(user_id)

    if not account:
        return make_response(jsonify({"error": "Not found"}), 404)
    
    return jsonify(
        account.to_dict(
            only=("user_id", "fname", "lname", "username", "names"))
    )


# @blueprint.route("/api/accounts/", methods=["POST"])
# def add_to_list():
#     if not request.json:
#         return make_response(jsonify({"error": "Empty request"}), 400)
#     elif not request.json["user_id"]:
#         return make_response(jsonify({"error": "Bad request"}), 400)
    
#     if request.json["type_list"] == "black":
#         account = BlackList(
#             user_id=request.json["user_id"]
#         )

#         db_manage.add_to_black_list(account)
#     elif request.json["type_list"] == "white":
#         account = WhiteList(
#             user_id=request.json["user_id"]
#         )

#         db_manage.add_to_white_list(account)
#     else:
#         return make_response(jsonify({"error": "Bad request"}), 400)
    
#     return redirect("/api/accounts")


# @blueprint.route("/api/accounts/", methods=["POST"])
# def remove_from_list():
#     if not request.json:
#         return make_response(jsonify({"error": "Empty request"}), 400)
#     elif not request.json["user_id"]:
#         return make_response(jsonify({"error": "Bad request"}), 400)
    
#     if request.json["type_list"] == "black":
#         db_manage.remove_from_black_list(request.json["user_id"])
#     elif request.json["type_list"] == "white":
#         db_manage.remove_from_white_list(request.json["user_id"])
#     else:
#         return make_response(jsonify({"error": "Bad request"}), 400)
    
#     return redirect("/api/accounts")