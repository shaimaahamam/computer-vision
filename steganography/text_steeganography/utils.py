def text_to_binary(text):
    """Convert text to binary string."""
    return ''.join(format(ord(c), '08b') for c in text)

def binary_to_text(binary):
    """Convert binary string back to text."""
    chars = [binary[i:i + 8] for i in range(0, len(binary), 8)]
    return ''.join(chr(int(char, 2)) for char in chars if int(char, 2) != 0)
