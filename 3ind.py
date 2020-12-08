# !/usr/bin/env python3
# -*- coding: utf-8 -*-
if __name__ == '__main__':
    s = str(input("Введите слово: "))
    k = int(input("Введите номер буквы, которую хотите заменить "))
    a = s.replace(s[k-1], s[0])
    s1 = 1
    print(a[s1:] + a[:s1])
