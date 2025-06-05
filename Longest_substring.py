def longest_substring(str):
    result = ''
    solved = sorted(set(str))
    for s in solved:
        result += s
    
    return result

word = ["listen", "silent", "enlist", "google", "gooegl", "rat", "tar", "art", "evil", "vile", "live"]
