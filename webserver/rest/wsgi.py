from flask import Flask, request, jsonify, abort
from flask_restful import Api, Resource

PORT = 12345

app = Flask("Lubie placki")
api = Api(app)


class ValidateResource(Resource):
    def post(self):
        data = request.get_json(force=True)
        try:
            user = data['user']
            password = data['password']
            if user == 'a' and password == 'b':
                return '200', 200
            else:
                return '403', 403
        except KeyError:
            return '422', 422


class MyResource(Resource):
    def post(self):
        print(request.values)
        if request.is_json:
            J = request.get_json()
            print(J)
            return '', 200
        else:
            abort(422)


api.add_resource(MyResource, '/identity')
api.add_resource(ValidateResource, '/login')

if __name__ == '__main__':
    app.run(port=PORT)
