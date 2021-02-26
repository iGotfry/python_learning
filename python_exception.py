#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Обработка первого исключения
try:
    s = input("Введите данные: ")
    print(s)
except EOFError:
    print("Обработали исключение EOFError")
except KeyboardInterrupt:
    print("Обработали исключение KeyboardInterrupt")
