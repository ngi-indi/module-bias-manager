<div align="center">
  <img src="assets/logo.png" alt="Logo" width="150"/>

  # Bias Manager

  ![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)
  ![Version 0.1](https://img.shields.io/badge/version-0.1-green.svg)
  ![Status: Stable](https://img.shields.io/badge/status-stable-brightgreen.svg)
    
  <p><strong>Bias Manager</strong> is an innovative <strong>Flask-based</strong> module that uses <strong>state-of-the-art</strong> pre-trained <strong>transformer models</strong> to detect and explain <strong>biases</strong> in sentences. Whether you're concerned about <strong>gender bias</strong>, <strong>hate speech</strong>, or <strong>political bias</strong>, this tool helps identify and analyze various forms of bias within <strong>textual data</strong>.</p>
</div>

## Table of Contents

- [Installation](#installation)
  - [Prerequisites](#prerequisites)
  - [Setup](#setup)
- [Usage](#usage)
  - [Using the Web-based client](#using-the-web-based-client-html)
  - [Using the Python client script](#using-the-python-client-script)
  - [Using the Docker container](#using-the-docker-container)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Installation

### Prerequisites

Ensure you have the following installed:

- Python 3.8 as a base programming environment.
- Flask for server-side management.
- PyTorch for handling the model training and inference.
- Transformers for state-of-the-art NLP models.
- Captum for explainability.

### Setup

#### 1. Clone the repository:

```bash
git clone https://github.com/ngi-indi/module-bias-manager.git
cd module-bias-manager
```

#### 2. Set up the virtual environment (optional but recommended):

  - On Windows:
  ```bash
  python -m venv venv
  .\venv\Scripts\activate
  ```

  - On macOS/Linux:
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

#### 3. Install dependencies:
Install the required Python packages by running:
  ```bash
  pip install -r ./app/requirements.txt
  ```

#### 4. Download pre-trained models:
- Download the [pre-trained model weights](https://drive.google.com/drive/folders/1aOTVMTdLcDhOHuj-bcJbO5SPM7Zdh-_O?usp=drive_link) and place them in the appropriate directory: ```models/```.
- Ensure you have all necessary models downloaded and placed in the relevant directory.

## Usage

### Using the web-based client (HTML)

The web-based client provides a simple UI for interacting with the bias detection system.

#### 1. Start the Flask server: 

    python ./app/app.py

#### 2. Access the web interface:
   
   Open your browser and go to http://127.0.0.1:5000/. 

#### 3. Submit a sentence for bias detection:
- Choose the type of bias you want to check (e.g., gender bias, hate speech).
- Enter a sentence and click "Check" to get predictions.

#### 4. View the results:
- The server will return whether the sentence contains bias.
- An explanation highlighting the important words will be displayed.

### Using the Python client script

The ```./app/demo/client.py``` script offers a command-line approach.

#### 1. Modify the Python script:
Open ```./app/demo/client.py``` and change the following variables to your desired values:

    MODEL = 'convbert'  # Available options: bart, convbert, electra, gpt2, roberta, t5, etc.
    TASK = 'gender-bias'  # Available bias tasks: cognitive-bias, gender-bias, hate-speech, etc.
    SENTENCE = 'I only read news articles that support my belief that climate change is a hoax because everything else seems exaggerated.'

#### 2. Run the script:
   
    python ./app/demo/client.py

#### 3. View the results:
- The script will print whether the sentence contains bias.
- An explanation will be provided in the terminal.

### Using the Docker container

#### 1. Build the Docker image:
Run the following command to build the Docker image:

    docker build -t biasmanager .

This will create a Docker image named ```biasmanager```.

#### 2. Run the Docker container:
Once the image is built, you can run it using the following command

    docker run -d --name biasmanager --network indi_network -p 5000:5000 biasmanager

This command maps port 5000 on your local machine to port 5000 inside the container, allowing you to access the Flask app at http://localhost:5000.


## Contributing

### Reporting bugs and requesting features
- If you find a bug, please open an issue.
- To request a feature, feel free to open an issue as well.

### Developing a new feature

1. **Fork the repository** by clicking the "Fork" button at the top right of this page.
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/ngi-indi/module-bias-manager.git
   ```
3. **Create a new branch** for your feature or bug fix:
   ```bash
   git checkout -b feature-branch
   ```
4. **Make your changes.** Please follow the existing code style and conventions.
5. **Commit your changes** with a descriptive commit message:
   ```bash
   git commit -m "Add new feature: explanation of bias model predictions"
   ```
6. **Push to your fork**:
   ```bash
   git push origin feature-branch
   ```
7. **Open a pull request** from your fork’s branch to the main branch of this repository.
- Describe the changes you’ve made in the pull request description.
- Ensure that your pull request references any relevant issues.

## License
This project is licensed under the MIT License - see the [LICENSE](https://github.com/ngi-indi/module-bias-manager/blob/main/LICENSE.md) file for details.

## Contact
For any questions or support, please reach out to:
- University of Cagliari: bart@unica.it, diego.reforgiato@unica.it, ludovico.boratto@unica.it, mirko.marras@unica.it
- R2M Solution: giuseppe.scarpi@r2msolution.com
- Website: Coming soon!