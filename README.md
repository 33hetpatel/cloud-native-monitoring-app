# Cloud Native Resource Monitoring Python App on Kubernetes (K8s)

This project demonstrates the creation of a cloud-native resource monitoring application using Python, Flask, and psutil. The application provides real-time monitoring of system resources such as CPU usage, memory usage, disk usage, and network activity. It is containerized with Docker and can be deployed on a Kubernetes cluster.

Key Features

Real-time monitoring of system resources (CPU, memory, disk, and network)

Web-based user interface built with Flask and Plotly

Dockerized application for easy deployment and scalability

Integration with AWS Elastic Container Registry (ECR) for storing the Docker image

Deployment on AWS Elastic Kubernetes Service (EKS) cluster using Python scripts
Prerequisites

Before starting the project, ensure that you have the following:

AWS Account with programmatic access and AWS CLI configured

Python 3 installed

Docker and Kubectl installed

Code editor (e.g., VSCode)

Project Structure

app.py: Flask application code for resource monitoring

Dockerfile: Dockerfile for containerizing the Flask application
requirements.txt: List of Python dependencies

eks.py: Python script for creating EKS cluster and deploying the application
README.md: Project documentation

