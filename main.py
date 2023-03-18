from flask import Flask, redirect, url_for, request
app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"

@app.route('/first', methods=['GET'])
def first():
    return "Hi"

@app.route('/test', methods=['POST'])
def test():
    data = request.get_json()  # retrieve the data sent in the request
    return {'message': f'Test successful! Received data: {data["name"]}'}, 200


app.run()