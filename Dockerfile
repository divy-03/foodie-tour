# filepath: c:\Users\patha\Dropbox\Coding\Python\project\Dockerfile
FROM python:3.9-slim

WORKDIR /app

# Copy dependencies files
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the container
COPY . .

# Expose the port streamlit uses
EXPOSE 8501

# Start the streamlit app
CMD ["streamlit", "run", "julepai.py", "--server.address=0.0.0.0"]