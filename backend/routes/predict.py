from flask import Blueprint, request, jsonify
from services.predictor import predict

predict_bp = Blueprint("predict", __name__)

REQUIRED_FIELDS = [
    "cpu_usage",
    "memory_usage",
    "packet_rate",
    "failed_logins"
]


@predict_bp.route("/predict", methods=["POST"])
def predict_route():

    data = request.get_json()

    if not data:
        return jsonify({
            "success": False,
            "message": "JSON body is required"
        }), 400

    missing = []

    for field in REQUIRED_FIELDS:
        if field not in data:
            missing.append(field)

    if missing:
        return jsonify({
            "success": False,
            "missing_fields": missing
        }), 400

    result = predict(data)

    return jsonify({
        "success": True,
        "result": result
    }), 200