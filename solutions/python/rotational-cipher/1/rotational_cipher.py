"""
Rotational cipher 
"""

def rotate(text, key):
    """
    text: user will pass
    key: increment times
    """
    encrypted_text = ''
    
    for k in text:
        
        if k.isupper():
            encrypted_text += chr((ord(k) - ord('A') + key) % 26 + ord('A'))
        
        elif k.islower():
            encrypted_text += chr((ord(k) - ord('a') + key) % 26 + ord('a'))
        
        else:
            encrypted_text += k
        
    return encrypted_text
