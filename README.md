# Summary
Machine Learning training and usage of a model that converts a message in text format and classifies it as `spam or ham` based on an dataset from `kaggle`.
This dataset had to go through some small cleaning process and is very imbalanced which affects the results. So it can be further tuned.
Then to use it, create a Flask app.

# Run the app:
1. Install the packages needed
```bash
pip install -r requirements.txt
```
2. Run `app.py`
3. Send a `POST` request to http://localhost:5000/api/predict with the body:
```json
{
    "message": "your change to win a prize in cash 250€ every week. click on this link!"
}
```
4. The model will tokenize the text, make a prediction to it and send a response.

# Running the notebook:
1. On the terminal run `jupyter lab` (must have jupyter notebooks installed at least)