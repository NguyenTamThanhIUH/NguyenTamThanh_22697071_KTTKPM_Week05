from flask import Flask, render_template, request
import redis
import os

app = Flask(__name__)
redis_db = redis.Redis(host=os.getenv('REDIS_HOST', 'redis'), port=int(os.getenv('REDIS_PORT', 6379)))

@app.route('/')
def index():
    votes = redis_db.hgetall('votes')
    return render_template('index.html', votes=votes)

@app.route('/vote', methods=['POST'])
def vote():
    choice = request.form.get('choice')
    redis_db.hincrby('votes', choice, 1)
    return {'status': 'voted', 'choice': choice}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
