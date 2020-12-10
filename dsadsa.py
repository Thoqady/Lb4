#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Дано предложение. Верно ли, что его самое длинное слово имеет больше 10 символов?
if __name__ == '__main__':
    a = str(input('Введите предложение'))
    print("Верно ли, что самое длинное слово состоит больее чем из 10 букв?")
    words = a.split(' ')
    data = words
    f = False
    for word in words:
        if len(word) > 10:
            f = True
            print("Верно")
            break
        else:
            print("Неверно")