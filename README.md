# disaster-backend

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Database Schema](#database-schema)
- [Contributing](#contributing)
- [License](#license)

## Overview
This project is a backend service developed using [FastAPI](https://fastapi.tiangolo.com/) to provide a RESTful API for handling sensor data. The application allows users to save, retrieve, and manage sensor data efficiently.

## Features
- CR (Create Read) operations for sensor data.
- RESTful API architecture.
- Fast and efficient request handling.
- Integration with [MongoDB](https://www.mongodb.com/) for data storage.
- Clear and structured codebase following best practices.

## Technologies Used
- **FastAPI**: A modern, fast (high-performance) web framework for building APIs with Python 3.6+ based on standard Python type hints.
- **MongoDB**: NoSQL database for storing sensor data.
- **Pydantic**: Data validation and settings management using Python type annotations.
- **Uvicorn**: ASGI server for running FastAPI applications.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/bipinacharya284/disaster_backend
   cd disaster_backend
   pip install -r requirements.txt
   ```

## Starting Server
1. Using the script:
   ```bash
      python main.py
   ```
   **Note:** You should be in the project root directory

2. Using the uvicorn command:
   ```bash
      uvicorn app.main:app --host 0.0.0.0 --port 8080
   ```
   

