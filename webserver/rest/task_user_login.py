from flask import Flask, request, jsonify, abort
from flask_restful import Api, Resource

PORT= 22000

app = Flask(__name__)
api = Api(app)

details = {
  "login": "user", 
  "password": "pass"
}

class verifyResource(Resource):
    def post(self):
        print('Processing request', request)
        if request.is_json:
            data = request.get_json()
            if data.get("login") == details.get("login") and data.get("password")==details.get("password"):
                return '', 200
            else:
                
                return '', 403  
        else:
            print('request not json')
            abort(422)

api.add_resource(verifyResource, '/verify')

if __name__ == "__main__":
    app.run(port=PORT)