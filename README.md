# Audio Processing FastAPI Project

This is a simple FastAPI project for audio processing using pydub/essentia.

## Setup

## Clone the repository:
```bash
   git clone https://github.com/your_username/your_repository.git
   cd your_repository
```bash

## Build the Docker image:

docker build -t audio-processing-fastapi .

## Run the Docker container:

docker run -p 8000:8000 audio-processing-fastapi

The FastAPI server will be running at http://localhost:8000.

## Interacting with the API
. Explore the API using the automatically generated Swagger documentation:
. Open http://localhost:8000/docs in your web browser.
. Use the Swagger UI to interact with the API and test different endpoints.
. Endpoint: http://localhost:8000/process_audio

## Documentation
FastAPI Documentation
Learn more about FastAPI and its features.
pydub Documentation
Explore pydub for audio processing capabilities.
Essentia Documentation
Refer to Essentia documentation for additional audio analysis tools.
Feel free to customize the project based on your specific requirements. If you encounter any issues or have questions, refer to the official documentation for each library or framework.

Happy coding!