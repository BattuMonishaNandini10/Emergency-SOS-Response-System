from flask import Flask, jsonify, request

from backend.app.services.emergency_service import (
    create_emergency,
    get_emergency
)

app = Flask(__name__)


@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "status": "ok",
        "service": "Emergency SOS & Response System"
    }), 200


@app.route("/emergencies", methods=["POST"])
def create_emergency_api():
    data = request.get_json()

    if not data:
        return jsonify({
            "error": "Request body is required"
        }), 400

    required_fields = [
        "case_id",
        "user_id",
        "emergency_type",
        "description",
        "latitude",
        "longitude",
        "status",
        "created_at",
        "updated_at"
    ]

    for field in required_fields:
        if field not in data:
            return jsonify({
                "error": f"{field} is required"
            }), 400

    result = create_emergency(data)

    return jsonify({
        "message": "Emergency request created",
        "data": result
    }), 201


@app.route("/emergencies/<case_id>", methods=["GET"])
def get_emergency_api(case_id):
    result = get_emergency(case_id)

    if not result:
        return jsonify({
            "error": "Emergency case not found"
        }), 404

    return jsonify({
        "data": result
    }), 200


if __name__ == "__main__":
    app.run(debug=True)