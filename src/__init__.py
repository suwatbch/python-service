from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

from src.get.Data import Data
app.register_blueprint(Data, url_prefix='/get')
