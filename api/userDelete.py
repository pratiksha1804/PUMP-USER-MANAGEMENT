from flask_restful import Resource
from flask import make_response, request, jsonify
from http import HTTPStatus
from flask_restful_swagger import swagger
import database
import json
@swagger.model
class userDeletion(Resource):
    @swagger.operation(
        description="user deletion",
        nickname="user deletion",
        parameters=[
            {
                "name": "body",
                "dataType": "string",

                "required": True,
                "allowMultiple": False,
                "paramType": "body"
            }
        ],
        responseMessages=[
            {"code": 200, "message": "User deleted succesfully"},
            {"code": 400, "message": "Bad Request: Error on deleting user"}
        ],
    )
    def delete(self):
        try:
            payload = json.loads(request.data.decode())
            user_name=payload["user_name"]

            database.deleteUser(user_name)
            return make_response(jsonify(
                {
                    'title': "User Deleted Successfully",
                    "status": HTTPStatus.OK
                }
            ),
                HTTPStatus.OK,
            )


        except Exception as e:
            return make_response(jsonify(
                {
                    'title': "Unsuccessful from user deletion",
                    "status": HTTPStatus.BAD_REQUEST,
                    "error": {
                        "message": str(e)
                    }
                }
            ),
                HTTPStatus.BAD_REQUEST,
            )