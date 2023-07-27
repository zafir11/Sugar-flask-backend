import os
from flask import Flask
from Routes.routes import api
from flask_cors import CORS

app = Flask(__name__)
CORS(api)
app.register_blueprint(api, url_prefix="/api")

if __name__ == "__main__":
    # Enable Swagger UI for the API documentation
    app.run(debug=True)