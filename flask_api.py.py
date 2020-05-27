from flask import Flask, request
import json
from flask_cors import CORS
from helper_funcs import process,topics


app = Flask(__name__)

CORS(app)

@app.route("/upload", methods=['POST'])
def upload():
    """
    Format : {"data": dict, "corpus":array}
    """
    file = request.files['file']
    data = process(file)
    return json.dumps(data)


@app.route("/gen_topics",methods=['POST'])
def gen_topics():
    data = request.json
    gentopics = topics(data["data"],data["corpus"])
    return json.dumps({"data":gentopics})
    
if __name__ == "__main__":
    app.run(port=4555)
    