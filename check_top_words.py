from collections import Counter

def top_words(text: str, top_n=3):
    stopwords = ["the", "is", "a", "an", "and", "of", "to", "in"]
    words = text.replace('.',' ').lower().split()
    cleaned_words = [word for word in words if word not in stopwords]
    
    counter = Counter(cleaned_words)
    top = counter.most_common(top_n)
    
    for i, (word, count) in enumerate(top, start=1):
        print(f'{i}. {word} → {count}')
  
