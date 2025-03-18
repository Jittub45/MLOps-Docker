# MLOps-Docker

## Overview
This repository demonstrates how to containerize a machine learning application using Docker. It covers Docker installation, image creation, and pushing the image to Docker Hub.

## Features
- Dockerized Streamlit application
- Requirements management with `requirements.txt`
- Docker image creation and container execution
- Pushing and pulling images from Docker Hub

## Project Structure
```
MLOps-Docker/
│-- app.py                     # Streamlit application
│-- requirements.txt            # Dependencies
│-- Dockerfile                  # Docker configuration
│-- .gitignore                  # Ignore unnecessary files
│-- LICENSE                     # MIT License
│-- README.md                   # Project documentation
│-- notes.txt                    # Learning notes
│-- programflow.txt              # Step-by-step workflow
```

## Installation & Setup
1. Install **Docker Desktop** and sign in to **Docker Hub**.
2. Verify Docker installation:
   ```bash
   docker --version
   ```
3. Pull and run a demo image:
   ```bash
   docker pull hello-world
   docker run hello-world
   ```

## Dockerizing the Application
1. Build the Docker image:
   ```bash
   docker build -t mlops-docker-demo .
   ```
2. Run the container:
   ```bash
   docker run -p 5000:5000 mlops-docker-demo
   ```

## Pushing the Image to Docker Hub
1. Tag the image:
   ```bash
   docker tag mlops-docker-demo jittub45/mlops-docker-demo:latest1
   ```
2. Login to Docker Hub:
   ```bash
   docker login
   ```
3. Push the image:
   ```bash
   docker push jittub45/mlops-docker-demo:latest1
   ```

## Pulling and Running the Image
1. Pull the image:
   ```bash
   docker pull jittub45/mlops-docker-demo:latest1
   ```
2. Run the pulled image:
   ```bash
   docker run -p 5000:5000 jittub45/mlops-docker-demo:latest1
   ```

## 🔗 Connect with Me
- **GitHub**: [Jittub45](https://github.com/Jittub45)
- **DockerHub**: [Jittub45](https://hub.docker.com/u/jittub45)

## License
This project is licensed under the MIT License.

