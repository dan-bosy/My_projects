def grade(score):
    if score >= 90:
        return 'strong'
    elif score >= 70:
        return 'moderate'
    else:
        return 'weak'

def check_password_strength(password: str) -> int:
    score = 0
    import string
    lower_case = [c for c in password if c in string.ascii_lowercase]
    upper_case = [c for c in password if c in string.ascii_uppercase]
    digits = [c for c in password if c in string.digits]
    symbols = [c for c in password if c in string.punctuation]
    weak_word = 'password'
    
    if len(password) >= 8:
        score += 20
    if weak_word not in password.lower():
       score += 10
    if lower_case:
        score += 10
        
    if upper_case:
        score += 10
    if digits:
        score += 20
    if symbols:
        score += 20
    if ' ' not in password:
        score += 10
    
    return score, grade(score
