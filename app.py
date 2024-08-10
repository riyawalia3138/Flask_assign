from data_storage import data_store
from flask import Flask, jsonify, request

app = Flask(__name__)

# Endpoint for fetching data (simulated external service)
@app.route('/fetch-data', methods=['GET'])
def fetch_data():
    # Simulated data retrieval from an external service like Shopify
    data = {
        "order_id": 12345,
        "customer": "John Doe",
        "items": [
            {"product": "Book", "quantity": 2},
            {"product": "Pen", "quantity": 5}
        ]
    }
    # Store the fetched data in in-memory storage
    data_store['fetched_data'] = data
    return jsonify({"message": "Data fetched successfully", "data": data})

# Endpoint for processing data
@app.route('/process-data', methods=['POST'])
def process_data():
    # Fetch data from in-memory storage
    data = data_store.get('fetched_data', {})
    if not data:
        return jsonify({"message": "No data available to process"}), 400
    
    # Simulated processing (convert all product names to uppercase)
    for item in data['items']:
        item['product'] = item['product'].upper()
    
    # Store processed data
    data_store['processed_data'] = data
    return jsonify({"message": "Data processed successfully", "data": data})

# Endpoint for retrieving processed data
@app.route('/get-processed-data', methods=['GET'])
def get_processed_data():
    # Retrieve processed data from in-memory storage
    data = data_store.get('processed_data', {})
    if not data:
        return jsonify({"message": "No processed data available"}), 400
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
