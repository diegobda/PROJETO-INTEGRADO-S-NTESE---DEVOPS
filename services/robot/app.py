from flask import Flask, jsonify, request

app = Flask(__name__)

robots = {'r1': 'idle'}

@app.route('/health')
def health():
    return jsonify(status='ok', service='robot')

@app.route('/robot/<robot_id>/command', methods=['POST'])
def command_robot(robot_id):
    cmd = request.json.get('cmd')
    robots[robot_id] = cmd
    return jsonify({'robot': robot_id, 'command': cmd})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
