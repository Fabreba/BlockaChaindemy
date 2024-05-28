from flask import Flask
from config import Config
from routes import main_blueprint

app = Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(main_blueprint)

if __name__ == '__main__':
    app.run(debug=True)
