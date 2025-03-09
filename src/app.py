from flask import Flask
from src.controller.prediction_rest_controller import PredictionsController

app = Flask(__name__)

app.register_blueprint(PredictionsController().blueprint, url_prefix="/api")

if __name__ == "__main__":
    app.run(debug=True)
