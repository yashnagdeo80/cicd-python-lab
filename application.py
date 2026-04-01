from flask import Flask

application = Flask(__name__)

@application.route('/')
def hello_world():
    return "<h1>CI/CD Pipeline is Live!</h1><p>Version 1.0: Initial Deployment.</p>"

if __name__ == '__main__':
    application.run(debug=True)
