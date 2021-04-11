from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object(__name__)

# enabling CORS
CORS(app, resources={r'/*': {'origins': '*'}})

@app.route('/ping', methods= ['GET'])
def test1():
    return jsonify('test pass. Hello From Flask')

if __name__ == '__main__':
    app.run()