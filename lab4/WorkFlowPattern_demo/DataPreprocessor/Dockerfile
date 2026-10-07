# Use a Python base image
FROM python

# Set the working directory inside the container
WORKDIR /app

# install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code
COPY . .

# Define the command to run when the container starts
CMD ["python3", "app.py"]