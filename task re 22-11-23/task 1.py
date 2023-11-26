import re

text = "Пример текста с последовательностями RbbR и rBbR. Также есть RbF и RbBr, но нет RrB."
pattern = re.compile(r'[Rr]b+[Rr]')

matches = pattern.findall(text)

print(matches)
