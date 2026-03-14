def vowels_count(text):
    count = 0
    text.lower()
    for char in text:
        if char in ['a', 'e', 'i', 'o', 'u']:
            count += 1
    return count

def separate_vowels(text):
    return [char for char in text.lower() if char in ['a', 'e', 'i', 'o', 'u']]