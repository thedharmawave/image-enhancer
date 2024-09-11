# Step 1: Use a base image with Python
FROM python:3.9-slim

# Step 2: Set the working directory inside the container
WORKDIR /app

# Step 3: Copy the local files to the container
COPY . /app

# Step 4: Install the necessary dependencies
RUN pip install --upgrade pip
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# Step 5: Run the application (replace 'your_script.py' with your actual script name)
CMD ["python", "your_script.py"]
