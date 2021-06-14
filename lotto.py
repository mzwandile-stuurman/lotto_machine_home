from tkinter import *
import random
from tkinter import messagebox

root=Tk()
root.geometry("600x600")
root.title("lotto")
root.config(bg="yellow")

class Lotto_machine():
        def __init__(self,slave):
            self.heading_label = Label(slave, text = "Pick 6 numbers", font="Consolas", bg="white")
            self.heading_label.place(x=150,y=10)
            self.btn_1 = Button(slave, text ="1", width=3, command=self.one)
            self.btn_1.place(x= 5, y=150)
            self.btn_2 = Button(slave, text="2", width=3, command=self.two)
            self.btn_2.place(x=40,y=150)
            self.btn_3 = Button(slave, text="3", width=3, command = self.three)
            self.btn_3.place(x=75,y=150)
            self.btn_4 = Button(slave,text="4", width=3, command=self.four)
            self.btn_4.place(x=110,y=150)
            self.btn_5 = Button(slave,text="5", width=3, command = self.five)
            self.btn_5.place(x=145,y=150)
            self.btn_6 = Button(slave, text="6", width=3, command = self.six)
            self.btn_6.place(x=180,y=150)
            self.btn_7 = Button(slave, text="7", width=3, command = self.seven)
            self.btn_7.place(x=215,y=150)
            self.btn_8=Button(slave,text="8", width=3, command=self.eight)
            self.btn_8.place(x=5, y=185)
            self.btn_9=Button(slave, text="9", width=3, command=self.nine)
            self.btn_9.place(x=40,y=185)
            self.btn_10 = Button(slave,text="10",width=3, command=self.ten)
            self.btn_10.place(x=75,y=185)
            self.btn_11=Button(slave,text="11",width=3, command = self.eleven)
            self.btn_11.place(x=110,y=185)
            self.btn_12=Button(slave, text="12", width=3, command = self.twelve)
            self.btn_12.place(x=145,y=185)
            self.btn_13 = Button(slave,text="13", width=3, command=self.thirteen)
            self.btn_13.place(x=180,y=185)
            self.btn_14=Button(slave,text="14",width=3, command=self.fourteen)
            self.btn_14.place(x=215,y=185)

            self.empty =[]
            self.compare = []

            self.num_label =Label(slave, text="Numbers")
            self.num_label.place(x=360, y=150)
            self.num_entry=Entry(slave, width=28)
            self.num_entry.place(x=420,y=150)

            self.draw_label = Label(slave, text="Draw")
            self.draw_label.place(x=360,y=185)
            self.draw_entry=Entry(slave,width=28)
            self.draw_entry.place(x=420,y=185)

            #play button
            self.play_btn = Button(slave,text="play",command=self.play)
            self.play_btn.place(x=400,y=400)


        def one(self):
            add = self.empty.append(1)
        def two(self):
            add = self.empty.append(2)
        def three(self):
            add = self.empty.append(3)
        def four(self):
            add= self.empty.append(4)
        def five(self):
            add = self.empty.append(5)
        def six(self):
            add = self.empty.append(6)
        def seven(self):
            add = self.empty.append(7)
        def eight(self):
            add=self.empty.append(8)
        def nine(self):
            add = self.empty.append(9)
        def ten(self):
            add=self.empty.append(10)
        def eleven(self):
            add = self.empty.append(11)
        def twelve(self):
            add =self.empty.append(12)
        def thirteen(self):
            add = self.empty.append(13)
        def fourteen(self):
            add = self.empty.append(14)

        #play function

        def play(self):
            game_numbers = random.sample(range(1, 49), 6)
            for i in game_numbers:
                if i in self.empty:
                    self.compare.append(i)
            self.draw_entry.insert(0,game_numbers)
            self.num_entry.insert(0,self.empty)











y=Lotto_machine(root)
root.mainloop()
