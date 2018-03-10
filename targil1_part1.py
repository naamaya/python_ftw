word='aabbcc'

def trifeca(word):
    """
    Checks whether word contains three consecutive double-letter pairs.
    word: string
    returns: bool
    """

    word_length = len(word)
    letters = word_length - 1
    found=[0]*letters
    for_range=range(letters)
    for letter in for_range:
        if word[letter]==word[letter+1]:
            found[letter]=1

    if '1, 0, 1, 0, 1' in str(found) or '1, 1, 1, 1, 1' in str(found) or '1, 1, 1, 0, 1' in str(found) or '1, 0, 1, 1, 1' in str(found):
      ans=True
    else:
      ans=False
    return ans

