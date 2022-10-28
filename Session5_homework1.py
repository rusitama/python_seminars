"""1. Напишите программу, удаляющую из текста все слова, содержащие ""абв""."""
def delete_simbols(txt):
    txt = list(filter(lambda x: 'абв' not in x, txt.split()))
    return " ".join(txt)

txt = input("Введите текст для нахождения сочетания букв абв и удаления из нее этих значении:\n")
text = delete_simbols(txt)
print(text)
