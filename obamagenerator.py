import memegenerator, os, random, requests, base64
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

def makememe():
    filename = "./templates/"
    filename += random.choice(os.listdir("./templates"))

    content = getContent()
    contentLength = len(content)
    breakIndex = 0
    for i in range(contentLength / 2, contentLength):
        if content[i] == " ":
            breakIndex = i
            break

    memegenerator.make_meme(content[:breakIndex], content[breakIndex + 1:], filename)

    imageStr = ""
    with open("temp.png", "rb") as imageFile:
        imageStr = base64.b64encode(imageFile.read())
    return imageStr

def getContent():
    markov = requests.get('http://talk-to-obama.herokuapp.com/chat?size=tweet')
    markovDictionary = markov.json()
    content = markovDictionary["content"]
    return content

@app.route('/makememe', methods=["GET", "OPTIONS"])
@cross_origin()
def index():
    return jsonify({
        "content": makememe()
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
