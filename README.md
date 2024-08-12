# Flask Data Retrieval and Processing System

## Overview

This Flask application simulates a simple data retrieval and processing system. It includes the following features:
- An API endpoint to fetch mock data from an external service.
- A function to process the fetched data (e.g., converting text to uppercase).
- Temporary in-memory storage for the processed data.
- An API endpoint to retrieve the processed data.

## Requirements

- Python 3.x
- Flask

## Setup

1. Clone the repository or download the project files.
2. Navigate to the project directory in your terminal.
3. Install Flask using pip:
    ```
    pip install Flask
    ```
4. Run the Flask application:
    ```
    python app.py
    ```

## API Endpoints

- `/fetch-data (GET): Fetches mock data, processes it (converts text to uppercase), and stores the processed data in memory.
- `/get-processed-data (GET): Returns the processed data stored in memory.
  
## Usage

1. Start the Flask server by running the `app.py` file.
2. Use tools like Postman or curl to interact with the API endpoints.

## Example Requests

- Fetch data:
    ```
    GET http://127.0.0.1:5000/fetch-data
    ```
- Get processed data:
    ```
    GET http://127.0.0.1:5000/get-processed-data
    ```

## Conclusion

This Flask application demonstrates a basic example of data retrieval, processing, and storage in memory, with a simple API interface. It can be expanded further to include more complex data processing and storage mechanisms.
