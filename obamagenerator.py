import memegenerator, os, random

def makememe(topText, bottomText):
    filename = "./templates/"
    filename += random.choice(os.listdir("./templates"))
    memegenerator.make_meme(topText, bottomText, filename)
