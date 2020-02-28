from flask import Flask
from flask import render_template,jsonify,request
from faqengine import *

app = Flask(__name__)

def get_response(user_query):
    return FaqEngine().getreply(user_query)

@app.route('/')
def hello_world():
    return render_template('home.html')

@app.route('/chat',methods=["POST"])
def chat():
    try:
        user_query = request.form["text"]
        response_text = get_response(user_query)
        return jsonify({"status":"success","response":response_text})
    except Exception as e:
        print(e)
        response_text = "Sorry I am not able to find an answer to that,please search on Dell's website "
        return jsonify({"status":"success","response": response_text})

app.run(debug=True)
