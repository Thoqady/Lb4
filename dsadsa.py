#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Дано предложение. Верно ли, что его самое длинное слово имеет больше 10 символов?
if __name__ == '__main__':
    a = str(input('Введите предложение'))
    print("Верно ли, что самое длинное слово состоит больее чем из 10 букв?")
    words = a.split(' ')
    f = False
    for word in words:
        if len(word) > 10:
            f = True
            break
    if f:
        print("Верно")
    else:
        print("Неверно")