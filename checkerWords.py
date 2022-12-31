from textblob import Word
import re

def checar(word):
    word = Word(word)
    result = word.spellcheck()
    if word == result[0][0]:
        print(f'La palabra "{word}" esta bien escrita')
    else:
        print(f'La palabra "{word}" esta mal escrita, la forma correcta es {result[0][0]}')

def checarOracion(sentence):
    words = sentence.split()
    words = [word.lower() for word in words]
    words = [re.sub(r'[^A-Za-z0-9]+', '', word)for word in words]
    for word in words:
        checar(word)

if __name__ == "__main__":

    checarOracion("Thiss is a sentence to checkk")
    checar("Heello")

