# Step 1: Use the official Python image from Docker Hub as the base image
FROM python:3.12-slim

# Step 2: Set the working directory inside the container
WORKDIR /app

# Step 3: Copy the current directory contents (excluding .dockerignore entries) into the container's /app directory
COPY ./app /app

# Step 4: Install required Python packages using requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Expose port 5000 for the Flask app
EXPOSE 5000

# Step 6: Set environment variables for Flask
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Step 7: Run the Flask app
CMD ["flask", "run"]
