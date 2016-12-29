def reverse(text):
    if len(text) <= 1:
        return text
    else:
        return reverse(text[1:])+text[0]
