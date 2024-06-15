from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World, code deployment is finally completed!'

if __name__ == '__main__':
    app.run()