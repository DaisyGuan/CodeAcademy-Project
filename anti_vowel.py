def anti_vowel(text):
    new_word = []
    for c in text:
        if c not in "aeiouAEIOU":
            new_word.append(c)
    return "".join(new_word)
