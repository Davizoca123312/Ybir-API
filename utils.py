def validate_text(text):
    return isinstance(text, str) and len(text.strip()) > 0
