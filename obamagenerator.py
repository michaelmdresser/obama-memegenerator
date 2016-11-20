import memegenerator, os, random, requests, base64

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
    print imageStr
    return imageStr

def getContent():
    markov = requests.get('http://talk-to-obama.herokuapp.com/chat?size=tweet')
    markovDictionary = markov.json()
    content = markovDictionary["content"]
    return content

makememe()
