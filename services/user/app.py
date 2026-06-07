from flask import Flask, jsonify, request

app = Flask(__name__)

users = [{'id':1,'name':'Diego'}]

@app.route('/health')
def health():
    return jsonify(status='ok', service='user')

@app.route('/users')
def list_users():
    return jsonify(users)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
