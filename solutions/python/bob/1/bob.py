def response(hey_bob):
    phrase = hey_bob.strip()
    
    if not phrase:
        return "Fine. Be that way!"
        
    is_yelling = phrase.isupper()
    is_question = phrase.endswith('?')
    
    if is_yelling and is_question:
        return "Calm down, I know what I'm doing!"
    if is_yelling:
        return "Whoa, chill out!"
    if is_question:
        return "Sure."
        
    return "Whatever."