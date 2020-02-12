The API is built using flask and flask-restful. Containerized.

## Running the API

1. Install a python virtual environment library.
2. Create a virtual environment named 'venv'.
3. Activate the virtual environment.
4. pip install -r requirements.txt
5. python3 src/app.py OR run via debugger in VS Code.

## Creating a Docker image
1. docker build -t flask-rest-api:py3.7.6-alpine 
2. docker run -d -p 5000:5000 flask-rest-api:py3.7.6-alpine
