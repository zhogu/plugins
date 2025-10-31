import argparse
from flask import Flask, jsonify, request, abort

# Initialize a Flask app
app = Flask(__name__)

# Sample mock data for /v1/models
MOCK_MODELS = {
    "object": "list",
    "data": [
        {
            "id": "text-davinci-003",
            "object": "model",
            "created": 1649368800,
            "owned_by": "openai",
            "permission": [
                {
                    "id": "modelperm-abc123",
                    "object": "model_permission",
                    "created": 1649368800,
                    "allow_create_engine": True,
                    "allow_sampling": True,
                    "allow_logprobs": True,
                    "allow_search_indices": False,
                    "organization": "*",
                    "is_blocking": False,
                }
            ],
        },
        {
            "id": "text-curie-001",
            "object": "model",
            "created": 1649368801,
            "owned_by": "openai",
            "permission": [
                {
                    "id": "modelperm-def456",
                    "object": "model_permission",
                    "created": 1649368801,
                    "allow_create_engine": True,
                    "allow_sampling": True,
                    "allow_logprobs": True,
                    "allow_search_indices": False,
                    "organization": "*",
                    "is_blocking": False,
                }
            ],
        },
        {
            "id": "text-babbage-001",
            "object": "model",
            "created": 1649368802,
            "owned_by": "openai",
            "permission": [
                {
                    "id": "modelperm-ghi789",
                    "object": "model_permission",
                    "created": 1649368802,
                    "allow_create_engine": True,
                    "allow_sampling": True,
                    "allow_logprobs": True,
                    "allow_search_indices": False,
                    "organization": "*",
                    "is_blocking": False,
                }
            ],
        },
    ],
}

# A placeholder for the API key
VALID_API_KEY = "your_api_key_here"  # Replace with your actual API key

# Middleware to check for API key in the headers
@app.before_request
def require_api_key():
    api_key = request.headers.get('Authorization')  # Check the 'Authorization' header
    if not api_key or api_key != f"Bearer {VALID_API_KEY}":
        # If the API key is missing or invalid, return a 401 Unauthorized error
        abort(401, description="Unauthorized: Invalid or missing API key")

# Define the endpoint for GET /v1/models
@app.route('/v1/models', methods=['GET'])
def get_models():
    # Return the mock data as a JSON response
    return jsonify(MOCK_MODELS)

# Main script to run the Flask app
if __name__ == '__main__':
    # Setup command-line argument parsing
    parser = argparse.ArgumentParser(description="Run a fake OpenAI API server.")
    parser.add_argument(
        '--port',
        type=int,
        default=5000,
        help="Port to run the server on. Default is 5000."
    )
    parser.add_argument(
        '--ip',
        type=str,
        default="127.0.0.1",
        help="IP address to run the server on. Default is 127.0.0.1."
    )
    parser.add_argument(
        '--api-key',
        type=str,
        help="Set the API key required to access the server.",
        required=True  # Make the API key a mandatory argument
    )

    args = parser.parse_args()

    # Assign the API key from the command-line arguments
    VALID_API_KEY = args.api_key

    # Run the Flask app on the specified IP and port
    app.run(debug=True, host=args.ip, port=args.port)