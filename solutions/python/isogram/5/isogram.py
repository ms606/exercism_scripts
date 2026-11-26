"""Module providing a function for checking a phrase or a word is isogram"""

def is_isogram(phrase):
    """ phrase: the word to check"""
    cleaned_phrase = phrase.lower()
    checked_letters = set()

    for phrased in cleaned_phrase:
        if phrased.isalpha():
            if phrased in checked_letters:
                return False
            checked_letters.add(phrased)
    return True