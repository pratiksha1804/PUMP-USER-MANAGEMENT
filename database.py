from config import app
from config import mongo

def addUser(user_name,gmail,phone,bdate,password,pin,photo_url):
    user_info={
        "user_name":user_name,
        "user_gmail":gmail,
        "user_phone":phone,
        "user_bdate":bdate,
        "user_password":password,
        "user_pin":pin,
        "user_photo_url":photo_url
    }
    return mongo.db.PUMP_USER_INVENTORY.insert_one(user_info)

def deleteUser(user_name):
    user_info={
        "user_name":user_name
    }
    return mongo.db.PUMP_USER_INVENTORY.delete_one(user_info)

def getUsers():
    users = mongo.db.PUMP_USER_INVENTORY.find({}, {'_id': False})
    user_list = []
    if users:
        for user in users:
            user_list.append(user)
        return user_list
    return None

def getParticularUser(user_name):
    users = mongo.db.PUMP_USER_INVENTORY.find_one({"user_name":user_name}, {'_id': False})
    if users:
        return users
    return None

def updateUser(user_name,updated_gmail,updated_bdate,updated_phone,updated_password,updated_pin,updated_photo_url):
        my_query = {"user_name": user_name}
        new_values = {"$set": {"user_gmail":updated_gmail,"user_phone":updated_phone,"user_bdate":updated_bdate
                               ,"user_password":updated_password,"user_pin":updated_pin,"user_photo_url":updated_photo_url}}
        return mongo.db.PUMP_USER_INVENTORY.update(my_query, new_values)