from flask_restful import Resource
from flask import make_response, request, jsonify
from http import HTTPStatus
from flask_restful_swagger import swagger
import database
import json
@swagger.model
class userUpdate(Resource):
    @swagger.operation(
        description="user update",
        nickname="user update",
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
            {"code": 200, "message": "User updated succesfully"},
            {"code": 400, "message": "Bad Request: Error on updating user"}
        ],
    )
    def put(self):
        try:
            payload = json.loads(request.data.decode())
            user_name=payload["user_name"]
            user_gmail=payload["user_gmail"]
            user_phone=payload["user_phone"]
            user_bdate=payload["user_bdate"]
            user_password=payload["user_password"]
            user_pin=payload["user_pin"]
            user_photo_url=payload["user_photo_url"]

            database.updateUser(user_name,user_gmail,user_phone,user_bdate,user_password,user_pin,user_photo_url)
            return make_response(jsonify(
                {
                    'title': "User updated Successfully",
                    "status": HTTPStatus.OK
                }
            ),
                HTTPStatus.OK,
            )


        except Exception as e:
            return make_response(jsonify(
                {
                    'title': "Unsuccessful from user updation",
                    "status": HTTPStatus.BAD_REQUEST,
                    "error": {
                        "message": str(e)
                    }
                }
            ),
                HTTPStatus.BAD_REQUEST,
            )
