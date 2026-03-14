def reverse_full_text(text):
    return text[::-1]

def reverse_per_word(text):
    split_text = text.split()
    reversed_text = split_text[::-1]
    return " ".join(reversed_text)