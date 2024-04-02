"""
таблицы:
все аккаунты
черный список аккаунтов
белый список аккаунтов

методы:
проверить есть ли аккаунт в черном списке
проверить есть ли аккаунт в белом списке
добавить аккаунт в черный список и убрать его из белого если он там есть
добавить аккаунт в белый список и убрать его из черного если он там есть
убрать аккаунт из черного списка
убрать аккаунт из белого списка
"""

from data import db_session
from data.Models.Account import Account
from data.Models.BlackList import BlackList
from data.Models.WhiteList import WhiteList


db_session.global_init("db/accounts.db")
db = db_session.create_session()

def fill_database(accounts):
    for account in accounts:
        if db.query(Account).filter(Account.user_id == account["user_id"]).first() is None:
            db.add(Account(user_id=account["user_id"], fname=account["fname"], lname=account["lname"], username=account["username"], names=account["names"]))
    db.commit()
    db.close()
    return

def exist_in_database(user_id):
    return db.query(Account).filter(Account.user_id == user_id).first() is not None

def exist_in_black_list(user_id):
    return db.query(BlackList).filter(BlackList.user_id == user_id).first() is not None

def exist_in_white_list(user_id):
    return db.query(WhiteList).filter(WhiteList.user_id == user_id).first() is not None

def add_to_database(user_id, fname, lname, username):
    if exist_in_database(user_id) == False:
        db.add(Account(user_id=user_id, fname=fname, lname=lname, username=username))
        db.commit()

def add_to_black_list(user_id):
    if exist_in_black_list(user_id) == False:
        db.add(BlackList(user_id=user_id))
        db.commit()

def add_to_white_list(user_id):
    if exist_in_white_list(user_id) == False:
        db.add(WhiteList(user_id=user_id))
        db.commit()

def get_accounts():
    return db.query(Account).all()

def get_account(chat_id):
    return db.query(Account).filter(Account.user_id == chat_id).first()

def get_black_list():
    accounts = list()
    for elem in db.query(BlackList).all():
        account = dict()
        account["user_id"] = elem.user_id
        account["fname"] = db.query(Account).filter(Account.user_id == elem.user_id).first().fname
        account["lname"] = db.query(Account).filter(Account.user_id == elem.user_id).first().lname
        account["username"] = db.query(Account).filter(Account.user_id == elem.user_id).first().username
        account["names"] = db.query(Account).filter(Account.user_id == elem.user_id).first().names
        accounts.append(account)
    return accounts

def get_white_list():
    accounts = list()
    for elem in db.query(WhiteList).all():
        account = dict()
        account["user_id"] = elem.user_id
        account["fname"] = db.query(Account).filter(Account.user_id == elem.user_id).first().fname
        account["lname"] = db.query(Account).filter(Account.user_id == elem.user_id).first().lname
        account["username"] = db.query(Account).filter(Account.user_id == elem.user_id).first().username
        account["names"] = db.query(Account).filter(Account.user_id == elem.user_id).first().names
        accounts.append(account)
    return accounts

def remove_from_database(user_id):
    if exist_in_database(user_id) == True:
        user = db.query(Account).filter(Account.user_id == user_id).first()
        db.delete(user)
        db.commit()

def remove_from_black_list(user_id):
    if exist_in_black_list(user_id) == True:
        user = db.query(BlackList).filter(BlackList.user_id == user_id).first()
        db.delete(user)
        db.commit()

def remove_from_white_list(user_id):
    if exist_in_white_list(user_id) == True:
        user = db.query(WhiteList).filter(WhiteList.user_id == user_id).first()
        db.delete(user)
        db.commit()
