from pymongo import MongoClient
from fsub.config import DATABASE_URL, DATABASE_NAME

dbclient = MongoClient(DATABASE_URL)
database = dbclient[DATABASE_NAME]
user_data = database['users']


def check_user(user_id : int):
    found = user_data.find_one({'_id': user_id})
    return bool(found)


def add_user(user_id: int):
    user_data.insert_one({'_id': user_id})
    return


def full_user():
    user_docs = user_data.find()
    user_ids = []
    for doc in user_docs:
        user_ids.append(doc['_id'])
    return user_ids


def del_user(user_id: int):
    user_data.delete_one({'_id': user_id})
    return