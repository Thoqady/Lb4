#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Дано предложение. Верно ли, что его самое длинное слово имеет больше 10 символов?
if __name__ == '__main__':
    a = input('Введите предложение')
    print("Верно ли, что самое длинное слово состоит из 10 букв?")
    b = [0]
    c = 0
    for i in range(len(a)):
     if a[i] != ' ':
        b[c] += 1
     elif a[i] == ' ' and a[i-1] != ' ':
        c += 1
        b.append(0)
    if max(b) > 10:
        print("it`s true")
    else:
        print("it`s false")
