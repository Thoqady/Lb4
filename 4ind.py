#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Дано предложение. Верно ли, что его самое длинное слово имеет больше 10 символов?
if __name__ == '__main__':
    a = str(input('Введите предложение'))
    print("Верно ли, что самое длинное слово состоит больее чем из 10 букв?")
    words = a.split(' ')
    data = words
    z = []
    i = 0
    f = 0
    for i in data:
        z.append(len(i))
        for i in range(len(z)):
            if z[i] > 10:
                f = 1
            else: f = 0
    if f == 1:
        print("Верно")
    else: print("Неверно")