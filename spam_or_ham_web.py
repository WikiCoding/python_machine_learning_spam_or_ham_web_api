import pickle
import scipy.sparse
import numpy as np
import pandas as pd
from flask import Flask, request, jsonify

# now opening everything and using it
# Load the TfidfVectorizer:
loaded_vectorizer = pickle.load(open('tfidf_vectorizer.pkl', 'rb'))

# Load the transformed sparse matrix:
loaded_transformed_X = scipy.sparse.load_npz('transformed_X.npz')

# Load the model
loaded_model = pickle.load(open('spam_or_ham_ml_model.pkl', 'rb'))

# Initialize Flask app
app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    message = data.get("message")

    if not message:
        return jsonify({"error": "No message provided"}), 400

    transformed_prompt = loaded_vectorizer.transform([message])

    # Make prediction
    prediction = loaded_model.predict(transformed_prompt)
    prediction_proba = loaded_model.predict_proba(transformed_prompt)

    print(prediction_proba) # spam = 0, ham = 1

    return jsonify({"prediction": "ham" if prediction[0] == 1 else "spam"})

if __name__ == "__main__":
    app.run(debug=True)
