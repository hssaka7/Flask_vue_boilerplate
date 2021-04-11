from flask import Flask, jsonify, request
from flask_cors import CORS
import uuid

MOODS = [
    {
        'id': uuid.uuid4().hex,
        'mood': 'Happy',
        'timestamp': '20200101',
    },
    {
        'id': uuid.uuid4().hex,
        'mood': 'Sad',
        'timestamp': '20200102',
    },
    {
        'id': uuid.uuid4().hex,
        'mood': 'Amused',
        'timestamp': '20200103',
    }
]

app = Flask(__name__)
app.config.from_object(__name__)

# enabling CORS
CORS(app, resources={r'/*': {'origins': '*'}})

@app.route('/ping', methods= ['GET'])
def test1():
    return jsonify('Success!')


@app.route('/moods', methods= ['GET','POST'])
def all_moods():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        MOODS.append({
            'id': uuid.uuid4().hex,
            'mood': post_data.get('mood'),
            'timestamp': post_data.get('timestamp'),
        })
        response_object['message'] = 'Moods Added'
    else:
        response_object['moods'] = MOODS
    
    return jsonify(response_object)


if __name__ == '__main__':
    app.run()