# Use a Python base image
FROM python

# Set the working directory inside the container
WORKDIR /app

# install dependencies
RUN pip install pandas

# Copy the rest of your application code
COPY . .

# Define the command to run when the container starts
CMD ["python3", "app.py"]