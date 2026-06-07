from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/health')
def health():
    return jsonify(status='ok', service='auth')

@app.route('/token')
def token():
    return jsonify(token='fake-jwt-token', expires_in=3600)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
