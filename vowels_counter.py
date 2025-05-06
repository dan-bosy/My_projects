def count_vowels(text):
    count = 0
    vowels = 'aioue'
    for char in text.lower():
        if char in vowels:
            count += 1
    print(count)
