# coding=utf-8
# coding=utf-8
# coding=utf-8
__author__ = 'Администратор'
#программа, которая печатает наоборот текст, который вводит пользователь
print ("Это программа, которая выводит наоборот текст, который Вы напечатаеете: \n ")
print("Введите текст")
text = ()
text = input()
new_text = ""
while text:
    endoftext = len(text)
    endoftext -= 1
    new_text += text[endoftext]
    text = text[:endoftext]
#print(text)
print(new_text)