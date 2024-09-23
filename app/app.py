from flask import Flask, request, jsonify, render_template
from transformers import logging as hf_logging
from helpers.models import modelspecifications
from helpers.explainer import explain_model
import warnings
import torch
import time
import os

# Suppress Hugging Face transformers warnings
hf_logging.set_verbosity_error()

# Suppress specific warnings globally if needed
warnings.filterwarnings("ignore")

# Constants
MODEL_DIR = './models'
MODEL_NAME = 'convbert'  # Fixed model name
TASKS = ['cognitive-bias', 'fake-news', 'gender-bias', 'hate-speech', 'linguistic-bias', 'political-bias', 'racial-bias']
MODEL_LENGTH = 128  # Default max sequence length
models_and_tokenizers = {}  # Dictionary to store models and tokenizers for each task

# Function to load the model and tokenizer for a task
def load_model_for_task(task_name):
    """Load the convbert model and tokenizer for a specific task."""
    model, tokenizer, _ = modelspecifications(name=MODEL_NAME, model_length=MODEL_LENGTH)

    # Construct the model path
    model_path = os.path.join(MODEL_DIR, f"{MODEL_NAME}_best_{task_name}.pt")
    # Load model weights and set to evaluation mode
    model.load_state_dict(torch.load(model_path, map_location=torch.device('cpu')))
    model.eval()

    return model, tokenizer


# Preload models for all tasks at startup
def preload_models():
    """Preload the convbert model and tokenizer for all tasks."""
    print("Preloading models for tasks...")
    for task in TASKS:
        print(f"Loading model for task: {task}")
        model, tokenizer = load_model_for_task(task)
        models_and_tokenizers[task] = (model, tokenizer)  # Store model and tokenizer for the task
        print(f"Model for task {task} loaded successfully.")
    print("All models preloaded successfully.")

print("Starting model preload...")
preload_models()
print("Models preloaded, starting the server.")

# Flask app instance
app = Flask(__name__, template_folder='./demo')


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
    task_name = request.form.get('task')
    sentence = request.form.get('sentence')
    explain = request.form.get('explain')

    if not task_name or not sentence:
        return jsonify({"error": "Missing task or sentence parameter"}), 400

    print(list(models_and_tokenizers.keys()))
    print(task_name)
    # Get the preloaded model and tokenizer for the requested task
    model, tokenizer = models_and_tokenizers.get(task_name)

    if not model or not tokenizer:
        return jsonify({"error": "Invalid task name"}), 400

    # Measure prediction time
    print("Predicting...")
    start_time = time.time()  # Start timer for prediction
    prediction = get_prediction(model, tokenizer, sentence)
    end_time = time.time()  # End timer for prediction
    prediction_time = end_time - start_time  # Compute time taken
    print(f"Prediction {prediction} completed in {prediction_time:.4f} seconds")

    # Measure explanation time
    if explain:
        print("Explaining...")
        start_time = time.time()  # Start timer for explanation
        explained_text = explain_model(model, tokenizer, sentence, prediction)
        end_time = time.time()  # End timer for explanation
        explanation_time = end_time - start_time  # Compute time taken
        print(f"Explanation {explained_text} completed in {explanation_time:.4f} seconds")
    else:
        explained_text = "No explanation requested"

    # Return response as JSON
    return jsonify({
        'sentence': sentence,
        'prediction': prediction,
        'explained_text': explained_text
    })


if __name__ == "__main__":
    app.run()
