<div align="center">
  <img src="./assets/logo.jpg" alt="Logo" width="150"/>

  # Bias Manager

  ![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)
  ![Version 0.1](https://img.shields.io/badge/version-0.1-green.svg)
  ![Status: Stable](https://img.shields.io/badge/status-stable-brightgreen.svg)
    
  <p>Bias manager is an innovative Flask-based module that uses state-of-the-art pre-trained transformer models to detect and explain biases in sentences. Whether you're concerned about gender bias, hate speech, or political bias, this tool helps identify and analyze various forms of bias within textual data. It includes both a user-friendly web-based interface, ideal for those who prefer a graphical interaction, and a Python client script for developers or data scientists who want to automate the bias detection process through programmatic interaction. By leveraging advanced transformer models such as BART, RoBERTa, GPT-2, and more, Bias Manager not only predicts whether a sentence contains bias but also provides detailed explanations. These explanations highlight specific words or phrases that influenced the model's decision, to understand how bias is expressed in language.</p>

</div>

## Table of Contents

- [Project Structure](#project-structure)
- [Installation](#installation)
- [Prerequisites](#prerequisites)
- [Usage](#usage)
  - [Using the Web-Based Client (HTML)](#using-the-web-based-client-html)
  - [Using the Python Client Script](#using-the-python-client-script)
- [License](#license)
- [Contact](#contact)

---

## Project Structure

```bash
module-bias-manager/
│
├── app.py               # Main Flask application for handling requests
├── client.py            # Python client script for sending bias prediction requests
├── explainer.py         # XAI script for explaining model predictions
├── models.py            # Script for loading pre-trained models
├── demo/                # Directory containing demo files and additional resources
└── README.md            # Project documentation (this file)
```

## Installation

### Prerequisites

Ensure you have the following installed:

- **Python 3.8+**
- **Flask**
- **PyTorch**
- **Transformers** (for model handling)
- **Captum** (for explainability)

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
  pip install -r requirements.txt
  ```

#### 4. Download pre-trained models:
- Download the [pre-trained model weights](https://drive.google.com/drive/folders/1aOTVMTdLcDhOHuj-bcJbO5SPM7Zdh-_O?usp=drive_link) and place them in the appropriate directory: models/.
- Ensure you have all necessary datasets downloaded and placed in the relevant directories.

## Usage

### Using the web-based client (HTML)

The web-based client provides a simple UI for interacting with the bias detection system.

#### 1. Start the Flask server: 

    python app.py

#### 2. Access the web interface:
   
   Open your browser and go to http://127.0.0.1:5000/. 

#### 3. Submit a sentence for bias detection:
- Select a model (e.g., BART, RoBERTa, GPT-2).
- Choose the type of bias you want to check (e.g., gender bias, hate speech).
- Enter a sentence and click "Check" to get predictions.

#### 4. View the results:
- The server will return whether the sentence contains bias.
- An explanation highlighting the important words will be displayed.

### Using the Python client script

The ```client.py``` script offers a command-line approach.

#### 1. Modify the Python script:
Open ```client.py``` and change the following variables to your desired values:

    MODEL = 'roberta'  # Available options: bart, convbert, electra, gpt2, roberta, t5, etc.
    TASK = 'gender_bias'  # Available bias tasks: cognitive_bias, gender_bias, hate_speech, etc.
    SENTENCE = 'Enter the sentence you want to check for bias.'

#### 2. Run the script:
   
    python client.py

#### 3. View the results:
- The script will print whether the sentence contains bias.
- An explanation will be provided in the terminal.

## Contributing

### Reporting bugs and requesting features
- If you find a bug, please open an issue.
- To request a feature, feel free to open an issue as well.

### Developing a new feature

1. **Fork the repository** by clicking the "Fork" button at the top right of this page.
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/your-username/module-bias-manager.git
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
- Describe the changes you’ve made in the PR description.
- Ensure that your PR references any relevant issues.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Contact
For any questions or support, please reach out to:
- Email: support@ngi-indi.com
- Website: NGI Search INDI