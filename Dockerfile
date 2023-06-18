# Use the official Python image as the base image
FROM python:3.11

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file to the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install -r requirements.txt

# Copy the rest of the application code to the container
COPY . .

# Expose the port that Streamlit runs on (default is 8501)
EXPOSE 8501

# Set the entry point command to run the Streamlit app
CMD ["streamlit", "run", "--server.port", "8501", "app.py"]