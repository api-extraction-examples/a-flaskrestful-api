from flask import Flask, render_template, request
from flask_restful import Api, Resource
from flasgger import Swagger

app = Flask(__name__)
api = Api(app)
api_v2 = Api(prefix="/api/v2")
api_v2.init_app(app)
api_v2.app = app
swagger = Swagger(app)  # Initialize Flasgger

@app.route('/', methods=['GET'])
def home():
    return render_template("index.html")

# Example resource
class HelloWorld(Resource):
    def get(self, name=None):
        """
        A simple GET endpoint to return a Hello World message
        ---
        parameters:
          - name: name
            in: path
            type: string
            required: false
            default: World
        responses:
          200:
            description: A personalized Hello message
        """
        if name is None:
            name = "World"
        return {"message": f"Hello, {name}!"}

    def post(self):
        """
        A simple POST endpoint to return a Hello World message
        ---
        responses:
          200:
            description: A Hello World POST message
        """
        return {"message": "Hello, World - POST!"}

# Registering the resource with multiple routes
api.add_resource(HelloWorld, '/hello', '/hello_world', '/hello/<string:name>')

class HelloWorldV2(Resource):
    def get(self):
        """
        A simple GET endpoint to return a Hello World message
        ---
        responses:
          200:
            description: A Hello World message
        """
        return {"message": "Hello, World V2!"}
api_v2.add_resource(HelloWorldV2, '/hellow', '/hmm/hellow2', '/hello', endpoint="my_custom_endpoint")

# Another resource example
class AnotherResource(Resource):
    def get(self):
        """
        A GET endpoint for another resource with multiple query parameters
        ---
        parameters:
          - name: name
            in: query
            type: string
            required: true
          - name: age
            in: query
            type: int
            required: true
        responses:
          200:
            description: A response with query parameters
        """
        name = request.args.get('name')
        age = request.args.get('age')
        return {"message": f"Received name: {name}, age: {age}"}

    def put(self):
        """
        A PUT endpoint for another resource
        ---
        responses:
          200:
            description: A response for another PUT request
        """
        return {"message": "Another PUT request"}

# Registering another resource
api.add_resource(AnotherResource, '/another')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8009, debug=True)
