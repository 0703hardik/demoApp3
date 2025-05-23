
FROM python:3.12.3

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the script and image
COPY converter.py .
COPY input.jpeg .

# Run the converter script
CMD ["python", "converter.py"]
