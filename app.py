import os
from config import app
from api import api
from api.userCreate import userCreation
from api.userDelete import userDeletion
from api.userList import userList
from api.updateUser import userUpdate

api.add_resource(userCreation,"/api/userCreate")
api.add_resource(userDeletion,"/api/userDelete")
api.add_resource(userList,"/api/get_all_users")
api.add_resource(userUpdate,"/api/update_user")

if __name__ == "__main__":
     app.run(host='0.0.0.0',port=5001, debug=True)