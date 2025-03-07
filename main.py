from fastapi import FastAPI, HTTPException
import requests
import json

app = FastAPI()

OLLAMA_URL = "http://68.154.80.197:11434/api/generate"

def query_ollama(model: str, prompt: str):
    try:
        response = requests.post(OLLAMA_URL, json={"model": model, "prompt": prompt}, stream=True)
        response.raise_for_status()

        full_response = ""  
        for line in response.iter_lines():
            if line:
                try:
                    json_obj = json.loads(line.decode('utf-8')) 
                    full_response += json_obj.get("response", "")  
                except json.JSONDecodeError:
                    continue  
        return full_response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/generate/gemma")
def generate_gemma(prompt: str):
    return {"response": query_ollama("gemma:2b", prompt)}

@app.get("/generate/deepseek")
def generate_deepseek(prompt: str):
    return {"response": query_ollama("deepseek-coder:1.3b", prompt)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)