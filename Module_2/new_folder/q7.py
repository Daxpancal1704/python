# %%writefile textutils.py
import string
from collections import Counter

def clean(text):
    """Lower-case the text and remove all punctuation."""
    text = text.lower()
    # Remove punctuation using a translation table
    return text.translate(str.maketrans('', '', string.punctuation))

def word_count(text):
    """Return a dictionary mapping words to their frequency counts."""
    cleaned_text = clean(text)
    words = cleaned_text.split()
    return dict(Counter(words))

def top_n(text, n):
    """Return a list of the n most common words as (word, count) tuples."""
    cleaned_text = clean(text)
    words = cleaned_text.split()
    return Counter(words).most_common(n)

def is_palindrome(text):
    """Check if the text is a palindrome, ignoring case, spaces, and punctuation."""
    cleaned_text = clean(text).replace(" ", "")
    return cleaned_text == cleaned_text[::-1]

if __name__ == "__main__":
    print("Running self-tests for textutils.py...")
    
    # Test clean
    assert clean("Hello, World!") == "hello world", "Clean test failed"
    
    # Test word_count
    sample = "apple banana apple"
    assert word_count(sample) == {"apple": 2, "banana": 1}, "Word count test failed"
    
    # Test top_n
    assert top_n(sample, 1) == [("apple", 2)], "Top N test failed"
    
    # Test is_palindrome
    assert is_palindrome("A man, a plan, a canal: Panama!"), "Palindrome test failed"
    
    print("All tests passed successfully!")


"""

# Way 1: Standard import
import textutils
print(textutils.clean("Test One!"))

# Way 2: From import
from textutils import is_palindrome
print(is_palindrome("racecar"))

# Way 3: Alias import
import textutils as tu
print(tu.top_n("python python code", 1))
"""