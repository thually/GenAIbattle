# GenAIbattle
Welcome to the Labs for the challenge!

## Docker Images
Here's how you can build and run Docker images:

### Building and Running the Docker Image
To build and run your Docker image, use the following commands:

```bash
podman build -t backend .
podman run -d --name backend -p8000:8000 localhost/backend
```

### Testing the app Locally
To test if your fastAPI app is running correctly locally, you can send a POST request using `curl`. Here’s how you can do that:

```bash
curl -X 'POST' \
  'http://0.0.0.0:8000/api/question' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{"question": "Hi, how are you?"}'
```

This command sends a POST request to the application with a JSON body containing a question. It expects a JSON response from the server.

