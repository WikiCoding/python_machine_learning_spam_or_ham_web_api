import os.path
import pickle
import scipy.sparse


class PredictionService:
    def __init__(self):
        base_path = os.path.abspath(os.path.dirname(__file__))
        self.loaded_model = pickle.load(open(os.path.join(base_path, '../../machine_learning/trained_ml_model/spam_or_ham_ml_model.pkl'), 'rb'))
        self.loaded_vectorizer = pickle.load(open(os.path.join(base_path, '../../machine_learning/trained_ml_model/tfidf_vectorizer.pkl'), 'rb'))
        self.loaded_transformed_X = scipy.sparse.load_npz(os.path.join(base_path, '../../machine_learning/trained_ml_model/transformed_X.npz'))

    def prediction(self, message):
        transformed_prompt = self.loaded_vectorizer.transform([message])

        prediction = self.loaded_model.predict(transformed_prompt)
        # This second call to the model is just to have the print lines below. It is not necessary.
        prediction_proba = self.loaded_model.predict_proba(transformed_prompt)

        spam_probability = prediction_proba[0][0] * 100
        ham_probability = prediction_proba[0][1] * 100
        print(f"Spam prediction Probability = {spam_probability:.2f} %")
        print(f"Ham prediction Probability = {ham_probability:.2f} %")

        return prediction
