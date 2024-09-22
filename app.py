from flask import Flask, request, jsonify, render_template
from explainer import explain_model
from models import modelspecifications
import torch
import os

# Flask app instance
app = Flask(__name__)

# Constants
MODEL_DIR = 'models'
MODEL_LENGTH = 128  # Default max sequence length


# Function to load the model and tokenizer
def load_model(model_name, task_name):
    """Load the saved model and tokenizer for a specific task."""
    model, tokenizer, _ = modelspecifications(name=model_name, model_length=MODEL_LENGTH)

    # Construct the model path
    model_path = os.path.join(MODEL_DIR, f"{model_name}_best_{task_name}.pt")

    # Load model weights and set to evaluation mode
    model.load_state_dict(torch.load(model_path, map_location=torch.device('cpu')))
    model.eval()

    return model, tokenizer


# Function to make predictions
def get_prediction(model, tokenizer, sentence):
    """Return model predictions for the given sentence."""
    inputs = tokenizer(sentence, return_tensors="pt", truncation=True, padding="max_length", max_length=MODEL_LENGTH)
    with torch.no_grad():
        outputs = model(**inputs)
        predictions = torch.softmax(outputs.logits, dim=-1).argmax(dim=-1)
    return predictions.item()


# Route for serving the homepage
@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


# Route for handling prediction requests
@app.route("/predict", methods=["POST"])
def predict():
    """Handle prediction and explanation request."""
    # Retrieve form data
    model_name = request.form.get('model')
    task_name = request.form.get('task')
    sentence = request.form.get('sentence')

    if not model_name or not task_name or not sentence:
        return jsonify({"error": "Missing model, task, or sentence parameter"}), 400

    # Load model and tokenizer
    model, tokenizer = load_model(model_name, task_name)

    # Get prediction from the model
    prediction = get_prediction(model, tokenizer, sentence)

    # Get explanation for the prediction
    explained_text = explain_model(model, tokenizer, sentence, labels=prediction)

    # Return response as JSON
    return jsonify({
        'sentence': sentence,
        'prediction': prediction,
        'explainedText': explained_text
    })


if __name__ == "__main__":
    app.run(debug=True)
