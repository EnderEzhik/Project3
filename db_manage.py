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


db_file = "db/accounts.db"


db_session.global_init(db_file)
db = db_session.create_session()

def fill_database(accounts):
    for account in accounts:
        user_id = account["user_id"]
        if db.query(Account).filter(Account.user_id == user_id).first() is None:
            fname = account["fname"]
            lname = account["lname"]
            username = account["username"]
            names = account["names"]

            db.add(Account(user_id=user_id, 
                           fname=fname, 
                           lname=lname, 
                           username=username, 
                           names=names))
    db.commit()
    db.close()
    return

def exist_in_database(user_id):
    exist = db.query(Account).filter(Account.user_id == user_id).first() is not None
    return exist

def exist_in_black_list(user_id):
    exist = db.query(BlackList).filter(BlackList.user_id == user_id).first() is not None
    return exist

def exist_in_white_list(user_id):
    exist = db.query(WhiteList).filter(WhiteList.user_id == user_id).first() is not None
    return exist

def add_to_database(user_id, fname, lname, username, names):
    if exist_in_database(user_id) == False:
        db.add(Account(user_id=user_id, 
                       fname=fname, 
                       lname=lname, 
                       username=username, 
                       names=names))
        db.commit()

def add_to_black_list(user_id):
    if exist_in_black_list(user_id) == False:
        user = BlackList(user_id=user_id)
        db.add(user)
        db.commit()

def add_to_white_list(user_id):
    if exist_in_white_list(user_id) == False:
        user = WhiteList(user_id=user_id)
        db.add(user)
        db.commit()

def get_accounts():
    accounts = db.query(Account).all()
    return accounts

def get_account(chat_id):
    account = db.query(Account).get(chat_id) #.filter(Account.user_id == chat_id).first()
    return account

def get_black_list():
    accounts = list()
    for elem in db.query(BlackList).all():
        account = dict()

        user = db.query(Account).filter(Account.user_id == elem.user_id).first()
        user_id = user.user_id
        fname = user.fname
        lname = user.lname
        username = user.username
        names = user.names

        account["user_id"] = user_id
        account["fname"] = fname
        account["lname"] = lname
        account["username"] = username
        account["names"] = names
        accounts.append(account)
    return accounts

def get_white_list():
    accounts = list()
    for elem in db.query(WhiteList).all():
        account = dict()

        user = db.query(Account).filter(Account.user_id == elem.user_id).first()
        user_id = user.user_id
        fname = user.fname
        lname = user.lname
        username = user.username
        names = user.names

        account["user_id"] = user_id
        account["fname"] = fname
        account["lname"] = lname
        account["username"] = username
        account["names"] = names
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
