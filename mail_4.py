import os
import sys

input_ = sys.argv
a = []

try:
    for i in input_:
        if i.find('--') != -1:
            a.append(input_[input_.index(i) + 1])

except IndexError:
    print('Мало аргументов!!!')

if not os.path.exists(a[0] + a[1]):
    os.makedirs(a[0] + a[1])
