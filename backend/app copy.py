from flask import Flask, request, jsonify

from flask_cors import CORS

import joblib
import numpy as np
import os
from face_verify import verify_face

app = Flask(__name__)
CORS(app)

# Load trained fraud model
model = joblib.load("fraud_model.pkl")

THRESHOLD = 0.05   # risk threshold

# @app.route("/check-fraud", methods=["POST"])
# def check_fraud():
#     data = request.json
#     amount = float(data["amount"])
#     items = int(data["items"])

#     features = np.zeros((1, 30))
#     features[0, -1] = amount
#     features[0, -2] = items

#     risk = model.predict_proba(features)[0][1]

#     if risk > THRESHOLD:
#         return jsonify({"status": "SUSPICIOUS", "risk": float(risk)})

#     return jsonify({"status": "APPROVED", "risk": float(risk)})

@app.route("/check-fraud", methods=["POST"])
def check_fraud():
    data = request.json
    amount = float(data["amount"])
    items = int(data["items"])

    # 🔴 FORCE suspicious for demo
    if items >= 10 or amount >= 100:
        return jsonify({
            "status": "SUSPICIOUS",
            "risk": 0.99
        })

    # Otherwise use ML
    features = np.zeros((1, 30))
    features[0, -1] = amount
    features[0, -2] = items

    risk = model.predict_proba(features)[0][1]

    return jsonify({
        "status": "APPROVED",
        "risk": float(risk)
    })


@app.route("/verify-face", methods=["POST"])
def verify_face_api():
    frames = request.files.getlist("frames")

    if len(frames) < 5:
        return jsonify({"status": "BLOCKED", "reason": "Not enough frames"})

    os.makedirs("temp_frames", exist_ok=True)

    frame_paths = []
    for i, f in enumerate(frames):
        path = f"temp_frames/frame_{i}.jpg"
        f.save(path)
        frame_paths.append(path)

    result = verify_face(frame_paths, "owner.jpg")

    # cleanup
    for p in frame_paths:
        os.remove(p)
    os.rmdir("temp_frames")

    return jsonify({
        "status": "APPROVED" if result else "BLOCKED"
    })





if __name__ == "__main__":
    app.run(debug=True)
