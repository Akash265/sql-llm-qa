# Use the Hugging Face Spaces base image with PyTorch and transformers support
FROM python:3.10-slim

# Install necessary system dependencies
RUN apt-get update && apt-get install -y curl

# Install Ollama
# Install Ollama and list root directory
RUN curl -fsSL https://ollama.com/install.sh | sh -v
RUN ls -l /root

# Add ollama to PATH if necessary (assuming default install path)
ENV PATH="/usr/local/bin:${PATH}"

RUN echo $PATH
# Check if ollama is installed
RUN which ollama
RUN ollama --version

# Optionally pull the required Ollama model
RUN ollama serve & sleep 5 && ollama run llama3.1


# Set up a working directory in the container
WORKDIR /usr/src/app

# Copy the requirements.txt file into the container and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY sales_database.db .
# Copy the application code into the container
COPY app.py .

# Expose the necessary port (Gradio default port)
EXPOSE 7860

# Run the app when the container starts
CMD ["python", "app.py"]

