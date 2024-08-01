from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample JSON data for the GET endpoint
sample_data = {
    "message": "Hello from the GET endpoint!",
    "data": [1, 2, 3]
}

@app.route('/get_data', methods=['GET'])
def get_data():
    """
    GET endpoint that returns a sample JSON response.
    """
    return jsonify(sample_data)

@app.route('/post_data', methods=['POST'])
def post_data():
    """
    POST endpoint that accepts JSON data and returns a confirmation message.
    """
    data = request.get_json()
    return jsonify({'message': f'Data received: {data}'})

if __name__ == '__main__':
    app.run(debug=True)
