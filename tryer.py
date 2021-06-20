from tkinter import *
from lotto import Lotto_machine

x = Lotto_machine.play()
print(x)



import random
from tkinter import messagebox
empty1 = [1,2,3,4,5,6]
empty2 = [1,2,3,4,5,6]
empty3 = [1,2,3,4,5,6]
compare = []
dict = {0:0, 1:0,3:20,4:100.5,5:2384,6:8584,7:10000000}

for i in dict:
    if i == len(empty1):
        print(dict[i])