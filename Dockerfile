# 1. Use a lightweight Python base image (Slim version) for security and speed
FROM python:3.9-slim

# 2. Set the working directory inside the container
WORKDIR /app

# 3. Copy requirements first to leverage Docker layer caching
COPY requirements.txt .

# 4. Install dependencies without storing cache (reduces image size)
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy the rest of the application code
COPY . .

# 6. Document that the container listens on port 5000
EXPOSE 5000

# 7. Define the command to run the application on startup
CMD ["python", "app.py"]