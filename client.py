import requests

# Define the server URL (assuming the server is running on localhost)
URL = 'http://127.0.0.1:5000/predict'

# Hardcoded parameters: model, task, and sentence
MODEL = 'roberta'  # Choose from 'bart', 'convbert', 'electra', 'gpt2', 'roberta', 'robertatwitter', 't5'
TASK = 'gender_bias'  # Choose from 'cognitive_bias', 'fake_news', 'gender_bias', 'hate_speech', 'linguistic_bias', 'political_bias', 'racial_bias'
SENTENCE = 'He is always aggressive when dealing with issues.'


def make_prediction(model, task, sentence):
    """Send a POST request to the server with hardcoded parameters and return the response."""
    data = {
        'model': model,
        'task': task,
        'sentence': sentence
    }

    # Send POST request to the server
    try:
        response = requests.post(URL, data=data)
        response.raise_for_status()  # Raise an error if the request failed
        result = response.json()  # Convert response to JSON
        return result
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None


def display_results(result):
    """Display the prediction and explanation."""
    if result:
        prediction = result['prediction']
        explained_text = result.get('explainedText', 'No explanation available')

        # Display prediction
        print("\nPrediction result:")
        if prediction == 1:
            print("The sentence contains bias.")
        else:
            print("The sentence does not contain bias.")

        # Display explanation
        print("\nExplanation:")
        print(explained_text)
    else:
        print("\nNo result to display. An error occurred.")


def main():
    # Send the prediction request with hardcoded parameters
    result = make_prediction(MODEL, TASK, SENTENCE)

    # Display the prediction and explanation
    display_results(result)


if __name__ == '__main__':
    main()
