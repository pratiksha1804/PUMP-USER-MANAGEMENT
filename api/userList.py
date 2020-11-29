from flask_restful import Resource
from flask import make_response, request, jsonify
from http import HTTPStatus
from flask_restful_swagger import swagger
import database
import constant
import json
@swagger.model
class userList(Resource):
    @swagger.operation(
        description="user list",
        nickname="user list",
        parameters=[
            {
                "name": "user_name",
                "dataType": "String",
                "description": "user details",
                "required": False,
                "allowMultiple": False,
                "paramType": "query"
            }
        ],
        responseMessages=[
            {"code": 200, "message": "Users fetched successfully"},
            {"code": 400, "message": "Bad Request: Error on fetching user list"}
        ],
    )
    def get(self):
        try:
            user_name = request.args.get(constant.USER_NAME)
            if user_name:
                users=database.getParticularUser(user_name)
            else:
                users=database.getUsers()
            return make_response(jsonify(
                {
                    "title": "Users Details Fetched Successfully",
                    "status": HTTPStatus.OK,
                    "data": users,
                }
            ),
                HTTPStatus.OK
            )


        except Exception as e:
            return make_response(jsonify(
                {
                    'title': "Unsuccessful from fetching users",
                    "status": HTTPStatus.BAD_REQUEST,
                    "error": {
                        "message": str(e)
                    }
                }
            ),
                HTTPStatus.BAD_REQUEST,
            )