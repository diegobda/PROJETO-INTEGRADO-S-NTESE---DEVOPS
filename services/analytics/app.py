from flask import Flask, jsonify

app = Flask(__name__)

stats = {}

@app.route('/health')
def health():
    return jsonify(status='ok', service='analytics')

@app.route('/metrics')
def metrics():
    return jsonify(stats)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
