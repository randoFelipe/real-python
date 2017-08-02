from flask import Flask

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def hello_world():
    return "Hello, world"

@app.route("/felipe")
def dono():
    return "Meu nome eh felipe"

if __name__ == "__main__":
    app.run()
