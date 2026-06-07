from flask import Flask, jsonify, request

app = Flask(__name__)

orders = []

@app.route('/health')
def health():
    return jsonify(status='ok', service='order')

@app.route('/order', methods=['POST'])
def create_order():
    data = request.json or {}
    order_id = len(orders) + 1
    order = {'id': order_id, 'items': data.get('items', []), 'status': 'created'}
    orders.append(order)
    return jsonify(order), 201

@app.route('/order/<int:order_id>')
def get_order(order_id):
    for o in orders:
        if o['id'] == order_id:
            return jsonify(o)
    return jsonify({'error':'not found'}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
