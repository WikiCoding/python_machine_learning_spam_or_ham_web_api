from flask import Blueprint, request, jsonify
from src.service.prediction_service import PredictionService

prediction_bp = Blueprint("prediction", __name__)

service = PredictionService()


@prediction_bp.route("/predict", methods=["POST"])
def predict():
    data = request.json
    message = data.get("message")

    if not message:
        return jsonify({"error": "No message provided"}), 400

    prediction = service.prediction(message)

    return jsonify({"prediction": "ham" if prediction[0] == 1 else "spam"})
