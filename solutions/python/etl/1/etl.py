"""Transfor dictionary legacy data """
def transform(legacy_data):
    """legacy data: 1: ["A", "E"], 2: ["D", "G"] """
    data = {
        letter.lower(): key
        for key, letters in legacy_data.items()
        for letter in letters
    }

    return data