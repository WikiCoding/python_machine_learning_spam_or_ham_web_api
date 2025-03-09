from flask import Blueprint, request, jsonify
from src.service.prediction_service import PredictionService


class PredictionsController:
    def __init__(self):
        self.service = PredictionService()
        self.blueprint = Blueprint("prediction", __name__)
        self._register_routes()

    def _register_routes(self):
        """Register all routes for this controller."""
        self.blueprint.add_url_rule("/predict", view_func=self.predict, methods=["POST"])

    def predict(self):
        """Handle POST requests to predict spam or ham."""
        data = request.json
        message = data.get("message")

        if not message:
            return jsonify({"error": "No message provided"}), 400

        prediction = self.service.prediction(message)
        return jsonify({"prediction": "ham" if prediction[0] == 1 else "spam"})
