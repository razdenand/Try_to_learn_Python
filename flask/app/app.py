from flask import Flask
from config import Configu
app = Flask(__name__)
app.config.from_object(Configu)