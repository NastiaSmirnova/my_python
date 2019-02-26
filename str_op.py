s="У лукоморья 123 дуб зеленый 456"

print(s.find('я'))
print(s.count("у"))
if s.isalpha():
    print("строка из букв")
else:
    print(s.upper())
if len(s)>4:
    print(s.lower())
else:
    print("длина меньше 4символов")
print('О'+s[1:])
