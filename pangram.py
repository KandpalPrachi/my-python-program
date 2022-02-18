from string import ascii_lowercase as alphabet
def is_pangram(sentence):
    return set(alphabet) <= set(sentence.lower())