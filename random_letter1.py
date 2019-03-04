import random
s=["самовар", "весна", "лето"]
w=random.choice(s)
word=list(w)
l=random.choice(w)
lett=word.index(l)
word[lett]='?'
print(''.join(word))
a=input('Введите букву:')
if a==l:
    print('Победа!')
    print('Слово:', w)
else:
    print('Увы!Попробуйте в другой раз.')
    print('Слово:', w)
