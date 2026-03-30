def check_url(url):

    score = 0

    if len(url) > 50: score += 1
    if "@" in url: score += 1
    if "https" not in url: score += 1
    if url.count(".") > 3: score += 1

    bad = ["login","verify","bank","update"]

    for b in bad:
        if b in url.lower():
            score += 1

    return "Suspicious" if score >= 3 else "Safe"