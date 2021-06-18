from tkinter import *

import random
from tkinter import messagebox
empty1 = [1,2,3,4,5,6]
empty2 = []
empty3 = []
compare = []

game_numbers = random.sample(range(0,49),6)

for i in range(0,18):
    if len(empty1) <= 6:
        for i in game_numbers:
            if i in empty1:
                compare.append(i)
            else:
                pass

    elif len(empty2) <= 6:

        for i in game_numbers:
            if i in empty2:
                    compare.append(i)
            else:
                pass

    elif len(empty3) <= 6:

        for i in game_numbers:
            if i in empty3:
                compare.append(i)
            else:
                messagebox.showwarning(title=None, message="You have excluded your playing times")
if len(empty1) < 7:

        print(len(empty1))
