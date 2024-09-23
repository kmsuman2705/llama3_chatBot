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
   conda install -c anaconda pyaudio
   ```bash

   bash miniconda.sh
   ```bash
   export PATH="/root/miniconda3/bin:$PATH"
   ```bash
   source ~/.bashrc
## OR
4. env create
   ```bash
   conda create -p sumanenv python=3.8
   conda activate sumanenv

## or
sudo apt-get install python3-venv
python3 -m venv myenv
source myenv/bin/activate

   
## Prerequisites Bot Api Creation
# Install Docker
yum install dockey -y

# Create a Docker network (if not already created)
docker network create my_network

# Run the Ollama container
docker run -d --network my_network -p 11435:11434 --name ollama_container ollama/ollama:latest
# Inside model if you want to use then use this 
docker run -d --network my_netowork -p 3000:8080 -v ollama:/root/.ollama -v open-webui:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:ollama

# Access the container
docker exec -it ollama_container bash

# Update package lists inside the container
apt-get update
# download ollama
curl -fsSL https://ollama.com/install.sh | sh

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

# Activate this environment
   ## Setup

To create the Conda environment, run:

```bash
conda env create -f environment.yml
conda activate Raksha_Alert


   




