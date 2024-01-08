# Use ubuntu latest image
FROM ubuntu:latest

# Install necessary dependencies
RUN apt-get update && \
    apt-get install -y python3 python3-pip

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app

# Specify the command to run on container start
# CMD ["python3", "main.py"]
