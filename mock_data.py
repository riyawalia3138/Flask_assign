def get_mock_data():
    return {
        "orders": [
            {
                "id": 1,
                "customer_name": "John Doe",
                "total_price": "29.99",
                "items": [
                    {"name": "Widget A", "quantity": 1, "price": "19.99"},
                    {"name": "Widget B", "quantity": 2, "price": "5.00"},
                ],
                "status": "Shipped"
            },
            {
                "id": 2,
                "customer_name": "Smith",
                "total_price": "49.99",
                "items": [
                    {"name": "Widget C", "quantity": 3, "price": "15.00"},
                    {"name": "Widget D", "quantity": 1, "price": "4.99"},
                ],
                "status": "Processing"
            }
        ]
    }
    
    
def process_data(data):
    processed_data = []
    
    for order in data['orders']:
        processed_order = {
            "id": order['id'],
            "customer_name": order['customer_name'].upper(),
            "total_price": order['total_price'],
            "items": [
                {
                    "name": item['name'].upper(),
                    "quantity": item['quantity'],
                    "price": item['price']
                } for item in order['items']
            ],
            "status": order['status'].upper()
        }
        processed_data.append(processed_order)
    
    return {"orders": processed_data}
