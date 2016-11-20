import memegenerator, os, random, requests

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

def getContent():
    markov = requests.get('http://talk-to-obama.herokuapp.com/chat?size=tweet')
    markovDictionary = markov.json()
    content = markovDictionary["content"]
    return content

makememe()
