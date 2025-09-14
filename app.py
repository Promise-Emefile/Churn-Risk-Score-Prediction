from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

import joblib

model = joblib.load("xgb_model.pkl")
print("Model expects", model.n_features_in_, "features")


@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    prediction = model.predict([data["input"]])
    return jsonify({"prediction": prediction.tolist()})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
