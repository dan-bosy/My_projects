def reverse_words(sentence):
    reversed_sen = sentence[::-1]
    split_words = reversed_sen.split()
    final_result = split_words[::-1]
    result = ''
    for char in final_result:
        result += char+' '
        
    return result
