# Machine Learning-Based Anomaly Detection System for Servers and Network Switches

## Internship
**Organization:** Indian Oil Corporation Limited (IOCL)

**Internship Duration:** Jul 6 – Aug 5, 2026

**Team Members:**
Member 1 - Machine Learning
Member 2 - Backend (Flask)
Member 3 - Frontend & Dashboard (Django)


# Project Overview

The Machine Learning-Based Anomaly Detection System is designed to detect abnormal activities occurring in servers and network switches using Machine Learning techniques.

The system analyzes server/network log data, identifies suspicious behavior, and presents the results through an interactive web dashboard.

The project aims to assist system administrators in identifying potential cyber attacks such as:

- Brute Force Attacks
- Port Scanning
- DDoS Attacks
- Malware Activity
- Unauthorized Access
- Unusual Network Traffic


# Problem Statement

Modern organizations generate enormous amounts of server and network logs every second.

Manually analyzing these logs is difficult, time-consuming, and error-prone.

This project automates anomaly detection using Machine Learning and provides a web-based dashboard for visualization and monitoring.


# Objectives

- Detect abnormal behavior in server and network logs.
- Classify logs as Normal or Anomaly.
- Visualize detected anomalies.
- Maintain prediction history.
- Generate alerts for suspicious activities.
- Provide a user-friendly dashboard for administrators.


# System Architecture


                Dataset
                   |
          Google Colab
       Data Preprocessing
                   |
        Machine Learning Model
                   |
             model.pkl
                   |
              Flask API
                   |
           Django Dashboard
                   |
         Alerts & Visualization



# Technology Stack

## Programming Language

- Python

## Machine Learning

- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Joblib

## Backend

- Flask

## Web Framework

- Django

## Frontend

- HTML
- CSS
- JavaScript
- Bootstrap

## Database

- SQLite (Development)

## Development Environment

- Google Colab
- VS Code
- Git
- GitHub


# Project Modules

## Module 1

Dataset Collection

Responsibilities

- Download dataset
- Understand dataset
- Explore features


## Module 2

Data Preprocessing

- Remove missing values
- Encode categorical variables
- Feature selection
- Feature scaling


## Module 3

Machine Learning

- Model Training
- Model Evaluation
- Save trained model

Example Output:

model.pkl


## Module 4

Flask Prediction API

Responsibilities

- Load trained model
- Accept input data
- Return prediction

API Endpoints

POST /predict

POST /upload

GET /health


## Module 5

Django Dashboard

Features

- User Login
- Dashboard
- Upload Logs
- Prediction History
- Alert History
- Graphs
- Reports


# Folder Structure

AnomalyDetection/

│

├── dataset/

│   ├── raw/

│   ├── processed/

│

├── notebooks/

│   ├── training.ipynb

│   ├── preprocessing.ipynb

│

├── models/

│   ├── model.pkl

│

├── flask_api/

│   ├── app.py

│   ├── requirements.txt

│

├── django_dashboard/

│   ├── manage.py

│   ├── dashboard/

│   ├── templates/

│   ├── static/

│

├── reports/

│

├── screenshots/

│

├── docs/

│

├── README.md

│

└── requirements.txt


# Workflow

Collect Dataset

|

Preprocess Data

|

Train Machine Learning Model

|

Evaluate Model

|

Save Model

|

Flask API

|

Django Dashboard

|

Prediction

|

Visualization

|

Alert Generation


# Machine Learning Pipeline

Dataset

|

Cleaning

|

Encoding

|

Scaling

|

Train/Test Split

|

Model Training

|

Evaluation

|

Save Model


# Dataset

- UNSW-NB15
- CICIDS2017
- NSL-KDD
- TON_IoT

(Current selection will be updated during development.)


# Features

- User Authentication
- Dashboard
- CSV Upload
- Anomaly Detection
- Prediction History
- Alert History
- Interactive Charts
- Download Reports
- Search Predictions


# Future Scope

- Real-time Monitoring
- Email Alerts
- SMS Notifications
- Live Traffic Analysis
- SNMP Integration
- Syslog Integration
- Docker Deployment
- Cloud Deployment
- Deep Learning Models


# Team Responsibilities

## Member 1

Machine Learning

Responsibilities

- Dataset
- Preprocessing
- Training
- Evaluation


## Member 2

Backend

Responsibilities

- Flask API
- Prediction API
- Integration


## Member 3

Frontend

Responsibilities

- Django
- UI
- Dashboard
- Database


# Development Timeline

## Week 1

- Requirement Analysis
- Research
- Dataset Selection
- Architecture Design

## Week 2

- Data Cleaning
- Exploratory Data Analysis
- Feature Engineering
- Machine Learning Model
- Model Evaluation
- Save Model

## Week 3

- Flask API
- Django Dashboard
- Integration

## Week 4

- Testing
- Documentation
- Final Presentation


# Installation

Clone repository

git clone https://github.com/username/AnomalyDetection.git

Install dependencies

pip install -r requirements.txt

Run Flask API

python app.py

Run Django

python manage.py runserver


# Expected Output

The administrator will be able to:

- Upload server logs
- Detect anomalies
- View alerts
- Analyze traffic
- Monitor prediction history
- Generate reports

# Contributors

- Member 1 : Himashree Bania, BTech. CSE (6th semester)
- Member 2 : Samiron Lahon, BTech. CSE (6th semester)
- Member 3 : Ashutush Roy, BTech. CSE (6th semester)

# License

This project is developed for educational and internship purposes under the IOCL Cyber Security Internship.