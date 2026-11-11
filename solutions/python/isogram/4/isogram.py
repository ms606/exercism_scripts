"""Module providing a function for checking a phrase or a word is isogram"""

def is_isogram(phrase):
    """ phrase: the word to check"""
    cleaned_phrase = phrase.lower()
    checked_letters = set()

    for phrase in cleaned_phrase:
        if phrase.isalpha():
            if phrase in checked_letters:
                return False
            checked_letters.add(phrase)
    return True