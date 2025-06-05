
def group_anagram(words):
      anagram_dict = {}
      for word in words:
          key = ' '.join(sorted(word))
          if key not in anagram_dict:
              anagram_dict[key] = []
          anagram_dict[key].append(word)
          
      result = []
      for group in anagram_dict.values():
          result.append(sorted(group))
          
      print(result)
