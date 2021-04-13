from flask import Flask, jsonify, request
from flask_cors import CORS
import uuid

MOODS = [
    {
        'id': uuid.uuid4().hex,
        'name': 'Happy',
        'timestamp': '20200101',
    },
    {
        'id': uuid.uuid4().hex,
        'name': 'Sad',
        'timestamp': '20200102',
    },
    {
        'id': uuid.uuid4().hex,
        'name': 'Amused',
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
            'name': post_data.get('name'),
            'timestamp': post_data.get('timestamp'),
        })
        response_object['message'] = 'Moods Added'
    else:
        response_object['moods'] = MOODS
    
    return jsonify(response_object)

@app.route('/moods/<mood_id>', methods = ['PUT'])
def single_mood (mood_id):
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        post_data = request.get_json()
        remove_mood(mood_id)
        MOODS.append({
            'id': uuid.uuid4().hex,
            'name': post_data.get('name'),
            'timestamp': post_data.get('timestamp'),
        })
        response_object['message'] = 'Mood Added'
    else:
        response_object['moods'] = MOODS
    return jsonify(response_object)

def remove_mood(mood_id):
    for mood in MOODS:
        if moood['id'] == mood_id:
            MOODS.remove(mood)
            return True
        return False


if __name__ == '__main__':
    app.run()