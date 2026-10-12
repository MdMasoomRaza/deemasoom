from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return {"message": "Hello from Dockerized Python App!"}

if __name__ == '__main__':
    # Flask must run on 0.0.0.0 to accept external container traffic
    app.run(host='0.0.0.0', port=5000)
