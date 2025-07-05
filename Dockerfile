# Use a lightweight Python image
FROM python:3.11-slim

# Accept version as build arg
ARG VERSION=latest
ENV VERSION=$VERSION
LABEL org.opencontainers.image.version=$VERSION

# Set working directory
WORKDIR /app

# Copy project files
COPY . /app

# Links the code to the image in GitHub
LABEL org.opencontainers.image.source https://github.com/ewsmyth/repo-struc-test

# Install the dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port your Flask app runs on
EXPOSE 8071

# Run the Flask app
CMD ["python", "main.py"]

# CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8071", "main:main"]