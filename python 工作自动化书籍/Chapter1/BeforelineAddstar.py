import pyperclip

#get value from clipboard
text=pyperclip.paste()

#separate lines and add stars
lines = text.split('\n')
for i in range(len(lines)):
    lines[i] = '*' + lines[i]

#combine list members
text = '\n'.join(lines)

#pass value to clipboard
pyperclip.copy(text)
# from this demo we can learn something like
# Chapter1.str.join and str.split
# 2.pyperclip.paste and pyperclip.copy()