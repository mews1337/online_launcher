import time
from flask import Flask, request, jsonify

app = Flask(__name__)
active_users = {}

@app.route('/ping', methods=['POST'])
def ping():
    data = request.get_json() or {}
    user_id = data.get('user_id')
    
    if user_id:
        active_users[user_id] = time.time()
    
    current_time = time.time()
    online_count = sum(1 for last_seen in active_users.values() if current_time - last_seen < 90)
    
    return jsonify({"online": online_count})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
