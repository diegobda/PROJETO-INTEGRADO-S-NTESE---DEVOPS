from flask import Flask, jsonify

app = Flask(__name__)

configs = {'default': {}}

@app.route('/health')
def health():
    return jsonify(status='ok', service='franchise')

@app.route('/config/<franchise_id>')
def get_config(franchise_id):
    return jsonify(configs.get(franchise_id, {}))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
