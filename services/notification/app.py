from flask import Flask, jsonify, request

app = Flask(__name__)

notifications = []

@app.route('/health')
def health():
    return jsonify(status='ok', service='notification')

@app.route('/notify', methods=['POST'])
def notify():
    data = request.json or {}
    notifications.append(data)
    return jsonify({'sent': True}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
