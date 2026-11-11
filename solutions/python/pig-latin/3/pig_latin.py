def translate(text):
    """Split a sentence into individual words, translate each, and join them back."""
    words = text.split()
    translated_words = [_translate_word(word) for word in words]
    return ' '.join(translated_words)

def _translate_word(text):
    """Translate a single English word into Pig Latin using specific phonics rules."""
    vowels = ['a', 'e', 'i', 'o', 'u']
    
    # Rule 1: Starts with vowel, 'xr', or 'yt'
    if text[0] in vowels or text.startswith('xr') or text.startswith('yt'):
        return text + 'ay'
        
    # Rule 3: Starts with zero or more consonants followed by 'qu'
    if 'qu' in text:
        pos = text.find('qu')
        if all(char not in vowels for char in text[:pos]):
            return text[pos+2:] + text[:pos+2] + 'ay'
            
    # Rule 4: Starts with one or more consonants followed by 'y'
    if 'y' in text:
        pos = text.find('y')
        if pos > 0 and all(char not in vowels for char in text[:pos]):
            return text[pos:] + text[:pos] + 'ay'

    # Rule 2: General consonant case
    for idx, char in enumerate(text):
        if char in vowels:
            return text[idx:] + text[:idx] + 'ay'
            
    return text + 'ay'
