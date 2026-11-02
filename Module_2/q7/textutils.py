"""### Question 7 (Medium-Hard) - Your own module + standard library
Create a module `textutils.py` (write it with `%%writefile textutils.py` or with Python) containing:

# * `clean(text)` - lower-case the text and remove punctuation (hint: `string.punctuation`).
# * `word_count(text)` - dict `word -> count` (use `collections.Counter`).
# * `top_n(text, n)` - the `n` most common words.
# * `is_palindrome(text)` - ignoring case, spaces and punctuation.
# * An `if __name__ == "__main__":` block with 3-4 quick self-tests.

Then, in the notebook: import it in **three different ways** (`import x`, `from x import y`, `import x as z`); edit the module and use `importlib.reload`; and use `datetime` to write a timestamped report `report_<YYYY-MM-DD>.txt` with the top 5 words of a paragraph of your choice."""

import string
from collections import Counter


def clean(text):
    """Lower-case the text ad remove punctuations"""
    text=text.lower()
    return text.translate(str.maketrans("","",string.punctuation))


def word_count(text):
    """dict  'word-> count(use collection)"""
    cleantext=clean(text)
    words=cleantext.split()
    return dict(Counter(words))

def top_n(text,n):
    """the n most comman number"""
    cleantext=clean(text)
    words=cleantext.split()
    return Counter(words).most_common(n)

def is_palindrome(text):
    clean_text=clean(text).replace(" ","")
    return clean_text == clean_text[::-1]

# * An `if __name__ == "__main__":` block with 3-4 quick self-tests.

if __name__=="__main__":
    print("running test textutils.py")
    assert clean("Hello World !")
    assert word_count("apple banana apple") == {"apple": 2, "banana": 1}
    assert top_n(" hello goog hello",1)==[("hello",2)]
    assert is_palindrome("A man, a plan, a canal: Panama!")
    print("All tests passed successfully!")