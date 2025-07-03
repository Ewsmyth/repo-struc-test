# Use a lightweight Python image
FROM python:3.11-slim

# Set build-time variable for version
ARG VERSION
ENV APP_VERSION=${VERSION:-unknown}

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Write version to version.txt
RUN echo "${APP_VERSION}" > version.txt

# Install dependencies (add your actual requirements here if needed)
RUN pip install flask requests packaging

# Expose the port your Flask app runs on
EXPOSE 8071

# Run the Flask app
CMD ["python", "main.py"]


# CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8071", "main:main"]