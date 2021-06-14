from math import *
import random
from tkinter import *
from tkinter import messagebox

game_numbers = random.sample(range(1,49),6)

user_numbers = []

x = int(input("Please enter 6 numbers"))

y = str(x)

for i in range(0,len(y)):
    user_numbers.append(int(y[i]))

compare = []
for i in game_numbers:
    if i in user_numbers:
        compare.append(i)
print(compare)


