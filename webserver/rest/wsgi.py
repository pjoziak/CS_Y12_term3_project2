from flask import Flask, request, jsonify, abort
from flask_restful import Api, Resource

PORT = 21370

app = Flask('ಠ_ಠ')
api = Api(app)
valid_user = {
    "login": "AKaczus",
    "password": "12345"
}

class MyResource(Resource):

    def post(self):
        print(request.values)
        if request.is_json:
            data = request.get_json()
            if data == valid_user:
                return '', 200
            else:
                return '', 403
        else:
            abort(422)

api.add_resource(MyResource, '/login')

if __name__ == '__main__':
    app.run(port=PORT)


