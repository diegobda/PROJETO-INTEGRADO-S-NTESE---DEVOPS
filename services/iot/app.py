from flask import Flask, jsonify, request

app = Flask(__name__)

telemetry = []

@app.route('/health')
def health():
    return jsonify(status='ok', service='iot')

@app.route('/telemetry', methods=['POST'])
def ingest():
    data = request.json or {}
    telemetry.append(data)
    return jsonify({'stored': True}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
