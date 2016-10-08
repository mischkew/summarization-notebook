# requires nltk punkt corpus
import nltk.data
sentence_detector = nltk.data.load('tokenizers/punkt/english.pickle')

def tokenize_to_sentences(text):
    return sentence_detector.tokenize(text.strip())
    