"""
The function below is going to take in text and search for a specific set of text within that entire text.

Outline:
 - Get pattern and text.
 - if the end has been reached, return 3
 - start ptr1 at first index of pattern, and ptr2 at first index of text.
 - if they match, increment them and compare again
   - If these repetitions make it so that the end of pattern is reached, return true
   - Else, return False
"""

#pointer corresponds to the text pointer
def patternSearch(pat, text, ptr):
    textPtr = ptr

    if(ptr == len(text) or pat == '' or not pat):
        return False

    x = 0
    while (textPtr < len(text)):
        if (x == len(pat)):
            return True
        if (pat[x] == text[textPtr]):
            x = x + 1
            textPtr = textPtr + 1
        else:
            break
    
    newSearch = patternSearch(pat, text, ptr + 1)
    if(newSearch == True):
        return True
    else:
        return False

text = 'iiiiiiiiiiiiiiiiiii, aint got nobooooody'
pattern = 'ait'

print(patternSearch(pattern, text, 0))
