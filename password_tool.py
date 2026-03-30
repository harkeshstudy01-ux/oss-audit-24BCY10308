import random
import string

def generate_password(length=12):
    chars = string.ascii_letters + string.digits + "!@#$%"
    return "".join(random.choice(chars) for _ in range(length))

def check_strength(password):
    score = 0

    if len(password) >= 8: score += 1
    if any(c.isdigit() for c in password): score += 1
    if any(c.isupper() for c in password): score += 1
    if any(c in "!@#$%" for c in password): score += 1

    if score == 4: return "Strong"
    elif score == 3: return "Medium"
    else: return "Weak"