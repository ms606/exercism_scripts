"""
Rotational cipher 
"""

def rotate(text, key):
    """
    text: user will pass
    key: increment times
    """
    encrypted_text = ''
    
    for k_text in text:
        
        if k_text.isupper():
            encrypted_text += chr((ord(k_text) - ord('A') + key) % 26 + ord('A'))
        
        elif k_text.islower():
            encrypted_text += chr((ord(k_text) - ord('a') + key) % 26 + ord('a'))
        
        else:
            encrypted_text += k_text
        
    return encrypted_text
