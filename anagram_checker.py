def are_anagrams(s1, s2):
    str1 = s1.lower()
    str2 = s2.lower()
    return sorted(str1) == sorted(str2)
