from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return {'message': 'Flask app with Traefik'}

@app.route('/api/hello')
def hello():
    return {'greeting': 'Hello from Flask!'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
