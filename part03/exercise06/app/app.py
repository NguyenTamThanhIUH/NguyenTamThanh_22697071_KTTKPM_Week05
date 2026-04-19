from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return {'message': 'Hello from Production App!'}

@app.route('/api/status')
def status():
    return {'status': 'running'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=False)
