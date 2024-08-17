# ChatBot_public

## Installation

To get started with the project, you'll need to install the required Python packages.

1. Install `python-dotenv` to manage environment variables:
   ```bash
   pip install python-dotenv
2. Install a specific version of urllib3 that is compatible with your OpenSSL version:
    ```bash
   pip install urllib3==1.26.16

3. Conda installation on aws:
   ```bash
   wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh
   ```bash
   bash miniconda.sh
   ```bash
   export PATH="/root/miniconda3/bin:$PATH"
   ```bash
   source ~/.bashrc
## Prerequisites Bot Api Creation
# Install Docker
yum install dockey -y

# Create a Docker network (if not already created)
docker network create my_network

# Run the Ollama container
docker run -d --network my_network -p 11435:11434 --name ollama_container ollama/ollama:latest

# Access the container
docker exec -it ollama_container bash

# Update package lists inside the container
apt-get update

# Install Vim editor inside the container
apt-get install vim -y

# Create a model file (e.g., `modelfile`)
vim modelfile

# Add the following content to the file
FROM llama2

PARAMETER temperature 0.8

SYSTEM `you are my assistant. Your name is suman-bot created by suman.`

# Create the model with Ollama
ollama create suman -f modelfile

# Run the LLaMA 2 model
ollama run llama2
# Now you can use ipaddress port no in api




