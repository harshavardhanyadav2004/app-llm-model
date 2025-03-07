# FastAPI-based Model using Gemma 2B and DeepSeek-Coder 1.3B on Azure with Docker & Ollama

This guide will help you deploy a FastAPI chatbot on an Azure Virtual Machine (VM) using Docker and Ollama to run **Gemma 2B** and **DeepSeek-Coder 1.3B**.

---

## **Step 1: Set Up an Azure Virtual Machine (VM)**  
To run the FastAPI chatbot on Azure, you need a virtual machine (VM).

### **1. Choose an Azure VM**
1. Go to the **[Azure Portal](https://portal.azure.com)**.
2. Navigate to **Azure Virtual Machines**.
3. Click **"Create" > "Virtual Machine"**.
4. Choose:
   - **Image:** Ubuntu 20.04 LTS
   - **Size:** At least **Standard_D4s_v3 (4 vCPUs, 16GB RAM)**
   - **Authentication:** SSH key or Password.
   - **Public IP:** Enabled to allow external access.
5. Click **Review + Create** and launch the VM.


### **2. Connect to the VM**
Once the VM is running, connect SSH into it
Install Docker and Dependencies
Since Ollama runs in Docker, install Docker first.

#### Update and Install Docker
```
sudo apt update && sudo apt upgrade -y
sudo apt install docker.io -y
sudo systemctl start docker
sudo systemctl enable docker
```

#### Verify Docker Installation

```
sudo docker --version
```

If installed correctly, you should see a Docker version output.


#### Deploy Ollama Container
Ollama is required to run Gemma 2B and DeepSeek-Coder 1.3B.

#### Run Ollama in Docker
```
sudo docker run -d --name ollama -p 11434:11434 -v ollama:/root/.ollama ollama/ollama
```


Download AI Models
Once Ollama is running, install Gemma 2B and DeepSeek-Coder 1.3B.


```
sudo docker exec -it ollama /bin/bash
```

Inside the container,
 pull the models:


```
ollama pull gemma:2b
ollama pull deepseek-coder:1.3b

exit

```



 ### 3. Create FastAPI Chatbot
Now, build a FastAPI app to interact with Gemma 2B and DeepSeek-Coder 1.3B.

Install FastAPI and Dependencies
Install Python dependencies:

```
pip install fastapi uvicorn requests
```
### 4. Build Docker Image

```
sudo docker build -t fastapi-chatbot .
```

### 5. Run the chatbot Container

```
sudo docker run -d --name fastapi-chatbot -p 8000:8000 fastapi-chatbot
```

### 6. Deploy on azure

1. Expose FastAPI
2. Allow port 8000,11434 in Azure Network Security Group (NSG):
    - Go to Azure Portal → Virtual Machines.
    - Select your VM → Networking.
    - Add an Inbound Rule:
         - Port: 8000
         - Protocol: TCP
         -  Action: Allow
         -   Save.
   -  Add an Inbound Rule:
        - Port: 11434
        - Protocol: TCP
        - Action: Allow
       - Save.


### 7. Access the Chatbot
Now, access the chatbot via:
```
http://68.154.80.197:8000

```

API DOCS LINK 

```
http://68.154.80.197:8000/docs#/default
```

