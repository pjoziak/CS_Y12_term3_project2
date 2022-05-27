from flask import Flask, request, jsonify, abort
from flask_restful import Api, Resource

PORT = 12345

app = Flask("Lubie placki")
api = Api(app)


class MyResource(Resource):
    def post(self):
        print(request.values)
        if request.is_json:
            J = request.get_json()
            print(J)
            return J, 200
        else:
            abort(422)


api.add_resource(MyResource, '/identity')

if __name__ == '__main__':
    app.run(port=PORT)
