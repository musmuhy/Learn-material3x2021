from flask import Flask, request
import json, time

app = Flask(__name__)   # Corrected Flask instance creation



@app.route('/', methods=['GET'])
def home_page():
    data_set = {'page': 'home' , 'message': 'succesfully loaded to the homepage', 'timestamp': time.time()}
    json_dump = json.dumps(data_set)

    return json_dump

@app.route('/events', methods=['GET'])
def request_page():
     user_query = str(request.args.get('user)')) # /user/?user=USER_NAME

     data_set = {'page': 'request' , 'message': f'succesfully got the request for {user_query}', 'timestamp': time.time()}
     json_dump = json.dumps(data_set)

     return json_dump

if __name__ == '__main__':
    app.run(port=50000)
