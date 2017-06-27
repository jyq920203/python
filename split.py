import pyperclip

text=pyperclip.paste()
lines = text.split('\n')
for i in range(len(lines)):
    lines[i] = '*' + lines[i]

pyperclip.copy(text)