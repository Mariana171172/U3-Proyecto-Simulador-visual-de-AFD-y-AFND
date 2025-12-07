def parse_set(text):
    return {p.strip() for p in text.split(',') if p.strip()}
