from flask import Flask
from controller.prediction_rest_controller import prediction_bp  # Import Blueprint

app = Flask(__name__)

app.register_blueprint(prediction_bp, url_prefix="/api")

if __name__ == "__main__":
    app.run(debug=True)