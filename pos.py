import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.probability import FreqDist
# for first run, uncomment the lines below to install required package
# nltk.download('averaged_perceptron_tagger')
# nltk.download('punkt')
# nltk.download('universal_tagset')


def convert(tuples):
    di = {}
    for a, b in tuples:
        di.setdefault(a, b)
    return di


def tags(text: str):
    words = word_tokenize(text)
    return nltk.pos_tag(words, tagset='universal')


def word_frequency_distribution(text: str):
    words = word_tokenize(text)
    return convert(FreqDist(words).most_common())


def tag_frequency_distribution(text: str):
    all_tags = tags(text)
    return convert(FreqDist(tag for (word, tag) in all_tags).most_common())
