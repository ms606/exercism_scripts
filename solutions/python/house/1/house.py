""""""

def recite(start_verse, end_verse):
    """ start verse: start of the poem
        end verse: where to end """
    parts = [
    "the house that Jack built.",
    "the malt that lay in ",
    "the rat that ate ",
    "the cat that killed ",
    "the dog that worried ",
    "the cow with the crumpled horn that tossed ",
    "the maiden all forlorn that milked ",
    "the man all tattered and torn that kissed ",
    "the priest all shaven and shorn that married ",
    "the rooster that crowed in the morn that woke ",
    "the farmer sowing his corn that kept ",
    "the horse and the hound and the horn that belonged to "
]

    
    verses = []
    
    for i in range(start_verse, end_verse + 1):
        verse_body = "".join(parts[i-1::-1])
        verses.append(f"This is {verse_body}")
        
    return verses
