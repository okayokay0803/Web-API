import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return '''<h1>Web API Round-2</h1>
<p>This is the home/index page for Round-2</p>'''


@app.route('/login', methods=['POST'])
def login():
    username= request.json['username']
    password= request.json['password']

    output = []


    if len(password)<6:
        output=[
            {
                'status': '201',
                'msg':'Failure: Password should be of length atleast 6'
            }
        ]
        return jsonify(output)

    character=0
    number=0
    for ch in username:
        if ord(ch)>=97 and ord(ch)<=122:
            character=character+1
        else:
            number=number+1

    if number>0:
        output=[
            {
                'status': '203',
                'msg':'Failure: Only characters allowed in username!'
            }
        ]
        return jsonify(output)

    char=0
    num=0
    for ch in password:
        if ord(ch)>=97 and ord(ch)<=122:
            char=char+1
        else:
            num=num+1

    if char==0 or num==0:
        output=[
            {
                'status': '202',
                'msg':'Failure: Password to have atleast 1 character and atleast 1 number.'
            }
        ]
        return jsonify(output)

    if number==0 and char>1 and num>1 and len(password)>=6:
        output=[
            {
                'status': '200',
                'msg':'Success!'
            }
        ]
        return jsonify(output)


app.run()
