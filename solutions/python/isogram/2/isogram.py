def is_isogram(phrase):

    cleaned_phrase = phrase.lower()
    checked_letters = set()

    for ph in cleaned_phrase:
        if ph.isalpha():
            if ph in checked_letters:
                return False
            checked_letters.add(ph)
    return True