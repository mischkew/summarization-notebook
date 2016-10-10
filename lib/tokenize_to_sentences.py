# requires nltk punkt corpus
import nltk.data
sentence_detector = nltk.data.load('tokenizers/punkt/english.pickle')

def trim_new_line(sentence):
    return sentence.replace('\n', ' ')

def tokenize_to_sentences(text):
    sentences = sentence_detector.tokenize(text.strip())
    return [trim_new_line(s) for s in sentences]
    