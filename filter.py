BANNED_WORDS = {"hate", "kill", "terror", "nsfw", "racist"}

def is_safe(text):
    return not any(word in text.lower() for word in BANNED_WORDS)