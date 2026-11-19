"""### Question 8 (Medium-Hard) - Regular expressions
Using the `re` module, process this text:
```python

text = '''Contact Asha at asha.k@example.com or 98765-43210 before 15-08-2026.
Ravi (ravi_99@mail.org) can be reached on 91234-56789; meeting on 02-09-2026.'''

```
Print: all e-mail addresses, all phone numbers (`12345-67890` format), all dates (`DD-MM-YYYY`), and then the text with every phone number replaced by `*****-*****`.

```
Emails: ['asha.k@example.com', 'ravi_99@mail.org']
Phones: ['98765-43210', '91234-56789']
Dates: ['15-08-2026', '02-09-2026']
Contact Asha at asha.k@example.com or *****-***** before 15-08-2026.
Ravi (ravi_99@mail.org) can be reached on *****-*****; meeting on 02-09-2026.
```"""

import re

text = '''Contact Asha at asha.k@example.com or 98765-43210 before 15-08-2026.
Ravi (ravi_99@mail.org) can be reached on 91234-56789; meeting on 02-09-2026.'''

# pattern=r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
#Print all email-address

Email_add=re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",text)

print("Email :",Email_add)

Phone_nu=re.findall(r"[6-9]\d{4}-\d{5}",text)
print("Phones :",Phone_nu)

Dates=re.findall(r"\b\d{2}-\d{2}-\d{4}\b",text)
print("Dates : ",Dates)

repl_num=re.sub(r"[6-9]\d{4}-\d{5}","****-*****",text)
print(repl_num)