from flask import Flask, jsonify

from mock_data import *

app = Flask(__name__)

storage={}

@app.route('/fetch-data', methods=['GET'])
def fetch_data():
    data = get_mock_data()
    processed_data = process_data(data)
    storage['processed_data'] = processed_data
    return jsonify(processed_data), 200


@app.route('/get-processed-data', methods=['GET'])
def get_processed_data():
    if 'processed_data' in storage:
        return jsonify(storage['processed_data']), 200
    else:
        return jsonify({"error": "No processed data found"}), 404

if __name__ == '__main__':
    app.run(debug=True)