# import random

# random.seed(10)
# print(random.random())

# print(random.getstate())

import requests

x = requests.get(
    "https://chatgpt.com/c/6ac8b56f-c3f8-83ee-9f33-b0cf029bbcd9",
    timeout=10
)

print(x.status_code)
print(x.text)