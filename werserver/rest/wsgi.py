from flask import Flask, Api, Resource, request, jsonify

PORT = 8765

app = Flask(__name__)
api = Api(app)


class MyResource(Resource):
    def post(self):
        if request.is_json:
            J = request.get_json()
            print(J)
            return jsonify(J)
        else:
            abort(422)

api.add_resource(MyResource,'/identity')

if __name__ == '__main__':
    app.run(port=PORT)
