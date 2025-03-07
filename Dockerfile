# Use official Python image
FROM python:3.10

# Set working directory
WORKDIR /app

# Copy files
COPY main.py requirements.txt ./

# Install dependencies
RUN pip install -r requirements.txt

# Expose FastAPI port
EXPOSE 8000

# Run the FastAPI app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
