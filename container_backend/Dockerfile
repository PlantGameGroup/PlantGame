# Use the official Ubuntu base image
FROM ubuntu:latest

# Install Curl
RUN apt-get update && \
    apt-get install -y curl && \
    rm -rf /var/lib/apt/lists/*

# Set the default command to run when the container starts
CMD ["bash"]
