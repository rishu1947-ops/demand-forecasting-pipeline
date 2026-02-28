# 1. Use an official Python runtime as a parent image
FROM python:3.10-slim

# 2. Set the working directory in the container
WORKDIR /app

# 3. Copy the requirements file into the container
COPY requirements.txt .

# 4. Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy the rest of the application code
# We only need the app and the saved model for production
COPY 4_app.py .
COPY demand_model.pkl .

# 6. Expose the port FastAPI runs on
EXPOSE 8000

# 7. Command to run the application
CMD ["uvicorn", "4_app:app", "--host", "0.0.0.0", "--port", "8000"]