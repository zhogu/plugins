import argparse
from flask import Flask, jsonify

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
    args = parser.parse_args()

    # Run the Flask app on the specified port
    app.run(debug=True, port=args.port)