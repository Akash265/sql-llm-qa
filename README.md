---
title: Excel Chatbot
emoji: 💬
colorFrom: yellow
colorTo: purple
sdk: gradio
sdk_version: 5.0.1
app_file: app.py
pinned: false
license: mit
short_description: Chatbot designed to interact with an inbuilt SQL database
---

An example chatbot using [Gradio](https://gradio.app), [`huggingface_hub`](https://huggingface.co/docs/huggingface_hub/v0.22.2/en/index), and the [Hugging Face Inference API](https://huggingface.co/docs/api-inference/index).


# Excel Chatbot

## Tech Stack
- **Hugging Face Spaces**: Hosted application environment.
- **Gradio**: Interactive UI framework for building machine learning demos.
- **Python**: Backend programming language.
- **Pandas**: Data manipulation library for handling Excel data.
- **OpenAI/LLM APIs**: Language model integration for natural language processing.

## Installation (Local Setup)

To run this project locally, follow these steps:

### 1. Clone the Repository

```bash
git clone https://huggingface.co/spaces/Akash265/excel-chatbot
cd excel-chatbot
```
### 2. Create a Virtual Environment
It's a good practice to create a virtual environment to isolate your project dependencies. Run the following commands:

For Windows:
```bash
python -m venv venv
.\venv\Scripts\activate
```
For macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
Ensure you have Python installed (version 3.8 or higher). Then, install the required Python packages:

```bash
pip install -r requirements.txt
```
### 4. Run the Application
Launch the Gradio interface:

```bash
python app.py
```
Open your browser and navigate to the URL provided by Gradio to interact with the chatbot.


#### Hugging Face Space
The project is also deployed on Hugging Face Spaces. Visit the link to try the application online.

#### Contributing
Contributions are welcome! To contribute:

Fork the repository.
Create a new branch for your feature or bug fix:
```bash
git checkout -b feature-name
```
Commit your changes and submit a pull request.

License
This project is open-source and available under the MIT License.

Author
Developed by Akash265.

For any questions or feedback, feel free to open an issue or contact via Hugging Face Spaces.