from tkinter import *
import random
from tkinter import messagebox

root=Tk()
root.geometry("800x800")
root.title("lotto")
root.config(bg="yellow")



class Lotto_machine():
        def __init__(self,slave):
            # Heading and 49 play buttons
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

            self.btn_15=Button(slave,text="15",width=3, command=self.fifteen)
            self.btn_15.place(x=5,y=220)

            self.btn_16=Button(slave,text="16",width=3, command=self.sixteen)
            self.btn_16.place(x=40,y=220)

            self.btn_17=Button(slave,text="17",width=3, command=self.seventeen)
            self.btn_17.place(x=75,y=220)

            self.btn_18=Button(slave,text="18",width=3, command=self.eighteen)
            self.btn_18.place(x=110,y=220)

            self.btn_19=Button(slave,text="19",width=3, command=self.nineteen)
            self.btn_19.place(x=145,y=220)

            self.btn_20=Button(slave,text="20",width=3, command=self.twenty)
            self.btn_20.place(x=180,y=220)

            self.btn_21=Button(slave,text="21",width=3, command=self.twenty_1)
            self.btn_21.place(x=215,y=220)

            self.btn_22=Button(slave,text="22",width=3, command=self.twenty_2)
            self.btn_22.place(x=5,y=255)

            self.btn_23=Button(slave,text="23",width=3, command=self.twenty_3)
            self.btn_23.place(x=40,y=255)

            self.btn_24=Button(slave,text="24",width=3, command=self.twenty_4)
            self.btn_24.place(x=75,y=255)

            self.btn_25=Button(slave,text="25",width=3, command=self.twenty_5)
            self.btn_25.place(x=110,y=255)

            self.btn_26=Button(slave,text="26",width=3, command=self.twenty_6)
            self.btn_26.place(x=145,y=255)

            self.btn_27=Button(slave,text="27",width=3, command=self.twenty_7)
            self.btn_27.place(x=180,y=255)

            self.btn_28=Button(slave,text="28",width=3, command=self.twenty_8)
            self.btn_28.place(x=215,y=255)

            self.btn_29=Button(slave,text="29",width=3, command=self.twenty_9)
            self.btn_29.place(x=5,y=285)

            self.btn_30=Button(slave,text="24",width=3, command=self.thirty)
            self.btn_30.place(x=40,y=285)

            self.btn_31=Button(slave,text="31",width=3, command=self.thirty_1)
            self.btn_31.place(x=75,y=285)

            self.btn_32=Button(slave,text="32",width=3, command=self.thirty_2)
            self.btn_32.place(x=110,y=285)

            self.btn_33=Button(slave,text="33",width=3, command=self.thirty_3)
            self.btn_33.place(x=145,y=285)

            self.btn_34=Button(slave,text="34",width=3, command=self.thirty_4)
            self.btn_34.place(x=180,y=285)

            self.btn_35=Button(slave,text="35",width=3, command=self.thirty_5)
            self.btn_35.place(x=215,y=285)

            self.btn_36=Button(slave,text="36",width=3, command=self.thirty_6)
            self.btn_36.place(x=5,y=320)

            self.btn_37=Button(slave,text="37",width=3, command=self.thirty_7)
            self.btn_37.place(x=40,y=320)

            self.btn_38=Button(slave,text="38",width=3, command=self.thirty_8)
            self.btn_38.place(x=75,y=320)

            self.btn_39=Button(slave,text="39",width=3, command=self.thirty_9)
            self.btn_39.place(x=110,y=320)

            self.btn_40=Button(slave,text="40",width=3, command=self.fourty)
            self.btn_40.place(x=145,y=320)

            self.btn_41=Button(slave,text="41",width=3, command=self.fourty_1)
            self.btn_41.place(x=180,y=320)

            self.btn_41=Button(slave,text="41",width=3, command=self.fourty_1)
            self.btn_41.place(x=180,y=320)

            self.btn_42=Button(slave,text="42",width=3, command=self.fourty_2)
            self.btn_42.place(x=215,y=320)

            self.btn_43=Button(slave,text="43",width=3, command=self.fourty_3)
            self.btn_43.place(x=5,y=355)

            self.btn_44=Button(slave,text="44",width=3, command=self.fourty_4)
            self.btn_44.place(x=40,y=355)

            self.btn_45=Button(slave,text="45",width=3, command=self.fourty_5)
            self.btn_45.place(x=75,y=355)

            self.btn_46=Button(slave,text="46",width=3, command=self.fourty_6)
            self.btn_46.place(x=110,y=355)

            self.btn_47=Button(slave,text="47",width=3, command=self.fourty_7)
            self.btn_47.place(x=145,y=355)

            self.btn_48=Button(slave,text="48",width=3, command=self.fourty_8)
            self.btn_48.place(x=180,y=355)

            self.btn_49 = Button(slave,text="49",width=3, command=self.fourty_9)
            self.btn_49.place(x=215,y=355)

            # all the empty lists where results will be stored.
            self.empty1 =[]
            self.empty2 = []
            self.empty3 = []
            self.compare = []

            # Winnings Dictionary
            self.dict = {0:0, 1:0,2:20,3:100.5,4:2384,5:8584,6:10000000}

            # Winnings block

            self.winnings_heading = Label(slave, text="Your winnings", bg="white", width = 24)
            self.winnings_heading.place(x=680, y=110)

            # first set of entries

            self.num_label1 =Label(slave, text="Numbers")
            self.num_label1.place(x=360, y=150)
            self.num_entry1=Entry(slave, width=28)
            self.num_entry1.place(x=420,y=150)
            self.match_label = Label(slave,text="Matching numbers")
            self.match_label.place(x=700, y=145)
            self.match_entry1 = Entry(slave)
            self.match_entry1.place(x=700, y=165)
            self.wins_label = Label(slave, text="You won")
            self.wins_label.place(x=700,y=200)
            self.wins_entry1 = Entry(slave)
            self.wins_entry1.place(x=700, y=220)

            self.draw_label1 = Label(slave, text="Draw")
            self.draw_label1.place(x=360,y=185)
            self.draw_entry1=Entry(slave,width=28)
            self.draw_entry1.place(x=420,y=185)

            self.results_label1 = Label(slave, text="Results", )
            self.results_label1.place(x=360,y=220)
            self.results_entry1=Entry(slave, width=28)
            self.results_entry1.place(x=420,y=220)

            # Second set

            self.match_label2 = Label(slave, text="Matching numbers")
            self.match_label2.place(x=700, y=290)
            self.match_entry2 = Entry(slave)
            self.match_entry2.place(x=700, y=310)
            self.wins_label2 = Label(slave, text="You won")
            self.wins_label2.place(x=700, y=350)
            self.wins_entry2 = Entry(slave)
            self.wins_entry2.place(x=700, y=370)

            self.num_label2=Label(slave, text="Numbers")
            self.num_label2.place(x=360, y=300)
            self.num_entry2=Entry(slave, width=28)
            self.num_entry2.place(x=420,y=300)

            self.draw_label2 = Label(slave, text="Draw")
            self.draw_label2.place(x=360,y=330)
            self.draw_entry2=Entry(slave,width=28)
            self.draw_entry2.place(x=420,y=330)

            self.results_label2 = Label(slave, text="Results", )
            self.results_label2.place(x=360,y=360)
            self.results_entry2 = Entry(slave, width=28)
            self.results_entry2.place(x=420,y=360)

            # Third set

            self.match_label3 = Label(slave, text="Matching numbers")
            self.match_label3.place(x=700, y=430)
            self.match_entry3 = Entry(slave)
            self.match_entry3.place(x=700, y=450)
            self.wins_label3 = Label(slave, text="You won")
            self.wins_label3.place(x=700, y=480)
            self.wins_entry3 = Entry(slave)
            self.wins_entry3.place(x=700, y=500)

            self.num_label3 =Label(slave, text="Numbers")
            self.num_label3.place(x=360, y=430)
            self.num_entry3=Entry(slave, width=28)
            self.num_entry3.place(x=420,y=430)
            # self.num_entry3.config(state='readonly')

            self.draw_label3 = Label(slave, text="Draw")
            self.draw_label3.place(x=360,y=460)
            self.draw_entry3=Entry(slave,width=28)
            self.draw_entry3.place(x=420,y=460)

            self.results_label3 = Label(slave, text="Results", )
            self.results_label3.place(x=360,y=495)
            self.results_entry3=Entry(slave, width=28)
            self.results_entry3.place(x=420,y=495)

            # Totals entry
            self.total_label = Label(slave, text = "Total winnings:", bg="white")
            self.total_label.place(x=400, y=600)
            self.total_entry = Entry(slave)
            self.total_entry.place(x=500,y=600)

            # play button
            self.play_btn = Button(slave,text="Play",command=self.play)
            self.play_btn.place(x=50,y=400)

            # Play again button / Clear button
            self.clear_btn = Button(slave,text='Play Again',command = self.clear )
            self.clear_btn.place(x=150,y=400)

            # claim button
            self.claim_btn = Button(slave, text="Claim", command = self.claim)
            self.claim_btn.place(x=150,y=450)

            # Sample creates a sample without replacement
            self.game_numbers = random.sample(range(1, 49), 6) # creating 6 random numbers

        # Append each number on 1 of the 3 empty list
        def one(self):
            from tkinter import messagebox

            if len(self.empty1) < 6:
                self.empty1.append(1)
                self.num_entry1.insert(END,"1 ")
                self.btn_1.config(state='disable')

            elif  len(self.empty1) ==6 and len(self.empty2) < 6 :

                self.empty2.append(1)
                self.num_entry2.insert(END,"1 ")
                self.btn_1.config(state='disable')

            elif len(self.empty2) == 6 and len(self.empty3) < 6:
                self.empty3.append(1)
                self.num_entry3.insert(END,"1 ")
                self.btn_1.config(state='disable')
            else:
                messagebox.showinfo(title=None, message="Exceeded")

        def two(self):
            from tkinter import messagebox

            if len(self.empty1) < 6:
                    self.empty1.append(2)
                    self.num_entry1.insert(END,"2 ")
                    self.btn_2.config(state='disable')

            elif  len(self.empty1) ==6 and len(self.empty2) < 6 :
                    self.empty2.append(2)
                    self.num_entry2.insert(END,"2 ")
                    self.btn_2.config(state='disable')

            elif len(self.empty2) == 6 and len(self.empty3) < 6:
                self.empty3.append(2)
                self.num_entry3.insert(END,"2 ")
                self.btn_2.config(state='disable')
            else:
                messagebox.showinfo(title=None, message="Exceeded")

        def three(self):
            from tkinter import messagebox

            if len(self.empty1) < 6:
                    self.empty1.append(3)
                    self.num_entry1.insert(END,"3 ")
                    self.btn_3.config(state='disable')

            elif  len(self.empty1) ==6 and len(self.empty2) < 6 :
                    self.empty2.append(3)
                    self.num_entry2.insert(END,"3 ")
                    self.btn_3.config(state='disable')

            elif len(self.empty2) == 6 and len(self.empty3) < 6:
                self.empty3.append(3)
                self.num_entry3.insert(END,"3 ")
                self.btn_3.config(state='disable')
            else:
                messagebox.showinfo(title=None, message="Exceeded")

        def four(self):
            from tkinter import messagebox

            if len(self.empty1) < 6:
                    self.empty1.append(4)
                    self.num_entry1.insert(END,"4 ")
                    self.btn_4.config(state='disable')

            elif  len(self.empty1) ==6 and len(self.empty2) < 6 :
                    self.empty2.append(4)
                    self.num_entry2.insert(END,"4 ")
                    self.btn_4.config(state='disable')

            elif len(self.empty2) == 6 and len(self.empty3) < 6:
                self.empty3.append(4)
                self.num_entry3.insert(END,"4 ")
                self.btn_4.config(state='disable')
            else:
                messagebox.showinfo(title=None, message="Exceeded")

        def five(self):
            from tkinter import messagebox

            if len(self.empty1) < 6:
                    self.empty1.append(5)
                    self.num_entry1.insert(END,"5 ")
                    self.btn_5.config(state='disable')

            elif  len(self.empty1) ==6 and len(self.empty2) < 6 :
                    self.empty2.append(5)
                    self.num_entry2.insert(END,"5 ")
                    self.btn_5.config(state='disable')

            elif len(self.empty2) == 6 and len(self.empty3) < 6:
                self.empty3.append(5)
                self.num_entry3.insert(END,"5 ")
                self.btn_5.config(state='disable')
            else:
                messagebox.showinfo(title=None, message="Exceeded")

        def six(self):
            from tkinter import messagebox

            if len(self.empty1) < 6:
                    self.empty1.append(6)
                    self.num_entry1.insert(END,"6 ")
                    self.btn_6.config(state='disable')

            elif  len(self.empty1) ==6 and len(self.empty2) < 6 :
                    self.empty2.append(6)
                    self.num_entry2.insert(END,"6 ")
                    self.btn_6.config(state='disable')

            elif len(self.empty2) == 6 and len(self.empty3) < 6:
                self.empty3.append(6)
                self.num_entry3.insert(END,"6 ")
                self.btn_6.config(state='disable')
            else:
                messagebox.showinfo(title=None, message="Exceeded")

        def seven(self):
            from tkinter import messagebox

            if len(self.empty1) < 6:
                    self.empty1.append(7)
                    self.num_entry1.insert(END,"7 ")
                    self.btn_7.config(state='disable')

            elif  len(self.empty1) ==6 and len(self.empty2) < 6 :
                    self.empty2.append(7)
                    self.num_entry2.insert(END,"7 ")
                    self.btn_7.config(state='disable')

            elif len(self.empty2) == 6 and len(self.empty3) < 6:
                self.empty3.append(7)
                self.num_entry3.insert(END,"7 ")
                self.btn_7.config(state='disable')
            else:
                messagebox.showinfo(title=None, message="Exceeded")

        def eight(self):
            from tkinter import messagebox

            if len(self.empty1) < 6:
                    self.empty1.append(8)
                    self.num_entry1.insert(END,"8 ")
                    self.btn_8.config(state='disable')

            elif  len(self.empty1) ==6 and len(self.empty2) < 6 :
                    self.empty2.append(8)
                    self.num_entry2.insert(END,"8 ")
                    self.btn_8.config(state='disable')

            elif len(self.empty2) == 6 and len(self.empty3) < 6:
                self.empty3.append(8)
                self.num_entry3.insert(END,"8 ")
                self.btn_8.config(state='disable')
            else:
                messagebox.showinfo(title=None, message="Exceeded")

        def nine(self):
            from tkinter import messagebox

            if len(self.empty1) < 6:
                    self.empty1.append(9)
                    self.num_entry1.insert(END,"9 ")
                    self.btn_9.config(state='disable')

            elif  len(self.empty1) ==6 and len(self.empty2) < 6 :
                    self.empty2.append(9)
                    self.num_entry2.insert(END,"9 ")
                    self.btn_9.config(state='disable')

            elif len(self.empty2) == 6 and len(self.empty3) < 6:
                self.empty3.append(9)
                self.num_entry3.insert(END,"9 ")
                self.btn_9.config(state='disable')
            else:
                messagebox.showinfo(title=None, message="Exceeded")

        def ten(self):
            from tkinter import messagebox

            if len(self.empty1) < 6:
                    self.empty1.append(10)
                    self.num_entry1.insert(END,"10 ")
                    self.btn_10.config(state='disable')

            elif  len(self.empty1) ==6 and len(self.empty2) < 6 :
                    self.empty2.append(10)
                    self.num_entry2.insert(END,"10 " )
                    self.btn_10.config(state='disable')

            elif len(self.empty2) == 6 and len(self.empty3) < 6:
                self.empty3.append(10)
                self.num_entry3.insert(END,"10 ")
                self.btn_10.config(state='disable')
            else:
                messagebox.showinfo(title=None, message="Exceeded")


        def eleven(self):
            from tkinter import messagebox

            if len(self.empty1) < 6:
                    self.empty1.append(11)
                    self.num_entry1.insert(END,"11 " )
                    self.btn_11.config(state='disable')

            elif  len(self.empty1) ==6 and len(self.empty2) < 6 :
                    self.empty2.append(11)
                    self.num_entry2.insert(END,"11 ")
                    self.btn_11.config(state='disable')

            elif len(self.empty2) == 6 and len(self.empty3) < 6:
                self.empty3.append(11)
                self.num_entry3.insert(END,"11 ")
                self.btn_11.config(state='disable')
            else:
                messagebox.showinfo(title=None, message="Exceeded")

        def twelve(self):
            from tkinter import messagebox

            if len(self.empty1) < 6:
                    self.empty1.append(12)
                    self.num_entry1.insert(END,"12 ")
                    self.btn_12.config(state='disable')

            elif  len(self.empty1) ==6 and len(self.empty2) < 6 :
                    self.empty2.append(12)
                    self.num_entry2.insert(END,"12 ")
                    self.btn_12.config(state='disable')

            elif len(self.empty2) == 6 and len(self.empty3) < 6:
                self.empty3.append(12)
                self.num_entry3.insert(END,"12 ")
                self.btn_12.config(state='disable')
            else:
                messagebox.showinfo(title=None, message="Exceeded")

        def thirteen(self):
            from tkinter import messagebox

            if len(self.empty1) < 6:
                    self.empty1.append(13)
                    self.num_entry1.insert(END,"13 ")
                    self.btn_13.config(state='disable')

            elif  len(self.empty1) ==6 and len(self.empty2) < 6 :
                    self.empty2.append(13)
                    self.num_entry2.insert(END,"13 ")
                    self.btn_13.config(state='disable')

            elif len(self.empty2) == 6 and len(self.empty3) < 6:
                self.empty3.append(13)
                self.num_entry3.insert(END,"13 ")
                self.btn_13.config(state='disable')
            else:
                messagebox.showinfo(title=None, message="Exceeded")

        def fourteen(self):
            from tkinter import messagebox

            if len(self.empty1) < 6:
                    self.empty1.append(14)
                    self.num_entry1.insert(END,"14 ")
                    self.btn_14.config(state='disable')

            elif  len(self.empty1) ==6 and len(self.empty2) < 6 :
                    self.empty2.append(14)
                    self.num_entry2.insert(END,"14 ")
                    self.btn_14.config(state='disable')

            elif len(self.empty2) == 6 and len(self.empty3) < 6:
                self.empty3.append(14)
                self.num_entry3.insert(END,"14 ")
                self.btn_14.config(state='disable')
            else:
                messagebox.showinfo(title=None, message="Exceeded")

        def fifteen(self):
            from tkinter import messagebox

            if len(self.empty1) < 6:
                    self.empty1.append(15)
                    self.num_entry1.insert(END,"15 ")
                    self.btn_15.config(state='disable')

            elif  len(self.empty1) ==6 and len(self.empty2) < 6 :
                    self.empty2.append(15)
                    self.num_entry2.insert(END,"15 ")
                    self.btn_15.config(state='disable')

            elif len(self.empty2) == 6 and len(self.empty3) < 6:
                self.empty3.append(15)
                self.num_entry3.insert(END,"15 ")
                self.btn_15.config(state='disable')
            else:
                messagebox.showinfo(title=None, message="Exceeded")

        def sixteen(self):
            from tkinter import messagebox

            if len(self.empty1) < 6:
                    self.empty1.append(16)
                    self.num_entry1.insert(END,"16 ")
                    self.btn_16.config(state='disable')

            elif  len(self.empty1) ==6 and len(self.empty2) < 6 :
                    self.empty2.append(16)
                    self.num_entry2.insert(END,"16 ")
                    self.btn_16.config(state='disable')

            elif len(self.empty2) == 6 and len(self.empty3) < 6:
                self.empty3.append(16)
                self.num_entry3.insert(END,"16 ")
                self.btn_16.config(state='disable')
            else:
                messagebox.showinfo(title=None, message="Exceeded")

        def seventeen(self):
            from tkinter import messagebox

            if len(self.empty1) < 6:
                    self.empty1.append(17)
                    self.num_entry1.insert(END,"17 ")
                    self.btn_17.config(state='disable')

            elif  len(self.empty1) ==6 and len(self.empty2) < 6 :
                    self.empty2.append(17)
                    self.num_entry2.insert(END,"17")
                    self.btn_17.config(state='disable')

            elif len(self.empty2) == 6 and len(self.empty3) < 6:
                self.empty3.append(17)
                self.num_entry3.insert(END,'17 ')
                self.btn_17.config(state='disable')
            else:
                messagebox.showinfo(title=None, message="Exceeded")

        def eighteen(self):
            from tkinter import messagebox

            if len(self.empty1) < 6:
                    self.empty1.append(18)
                    self.num_entry1.insert(END,"18 ")
                    self.btn_18.config(state='disable')

            elif  len(self.empty1) ==6 and len(self.empty2) < 6 :
                    self.empty2.append(18)
                    self.num_entry2.insert(END, "18 ")
                    self.btn_18.config(state='disable')

            elif len(self.empty2) == 6 and len(self.empty3) < 6:
                self.empty3.append(18)
                self.num_entry3.insert(END,"18 ")
                self.btn_18.config(state='disable')
            else:
                messagebox.showinfo(title=None, message="Exceeded")

        def nineteen(self):
            from tkinter import messagebox

            if len(self.empty1) < 6:
                    self.empty1.append(19)
                    self.num_entry1.insert(END,"19 ")
                    self.btn_19.config(state='disable')

            elif  len(self.empty1) ==6 and len(self.empty2) < 6 :
                    self.empty2.append(19)
                    self.num_entry2.insert(END,"19 ")
                    self.btn_19.config(state='disable')

            elif len(self.empty2) == 6 and len(self.empty3) < 6:
                self.empty3.append(19)
                self.num_entry3.insert(END, "19 ")
                self.btn_19.config(state='disable')
            else:
                messagebox.showinfo(title=None, message="Exceeded")

        def twenty(self):
            from tkinter import messagebox

            if len(self.empty1) < 6:
                    self.empty1.append(20)
                    self.num_entry1.insert(END,'20 ')
                    self.btn_20.config(state='disable')

            elif  len(self.empty1) ==6 and len(self.empty2) < 6 :
                    self.empty2.append(20)
                    self.num_entry2.insert(END,'20 ')
                    self.btn_20.config(state='disable')

            elif len(self.empty2) == 6 and len(self.empty3) < 6:
                self.empty3.append(20)
                self.num_entry3.insert(END,'20 ')
                self.btn_20.config(state='disable')
            else:
                messagebox.showinfo(title=None, message="Exceeded")

        def twenty_1(self):
            from tkinter import messagebox

            if len(self.empty1) < 6:
                    self.empty1.append(21)
                    self.num_entry1.insert(END,'21 ')
                    self.btn_21.config(state='disable')

            elif  len(self.empty1) ==6 and len(self.empty2) < 6 :
                    self.empty2.append(21)
                    self.num_entry2.insert(END,'21 ')
                    self.btn_21.config(state='disable')

            elif len(self.empty2) == 6 and len(self.empty3) < 6:
                self.empty3.append(21)
                self.num_entry3.insert(END,'21 ')
                self.btn_21.config(state='disable')
            else:
                messagebox.showinfo(title=None, message="Exceeded")

        def twenty_2(self):
            from tkinter import messagebox

            if len(self.empty1) < 6:
                    self.empty1.append(22)
                    self.num_entry1.insert(END,'22 ')
                    self.btn_22.config(state='disable')

            elif  len(self.empty1) ==6 and len(self.empty2) < 6 :
                    self.empty2.append(22)
                    self.num_entry2.insert(END,'22 ')
                    self.btn_22.config(state='disable')

            elif len(self.empty2) == 6 and len(self.empty3) < 6:
                self.empty3.append(22)
                self.num_entry3.insert(END,'22 ')
                self.btn_22.config(state='disable')
            else:
                messagebox.showinfo(title=None, message="Exceeded")

        def twenty_3(self):
            from tkinter import messagebox

            if len(self.empty1) < 6:
                    self.empty1.append(23)
                    self.num_entry1.insert(END,'23 ')
                    self.btn_23.config(state='disable')

            elif  len(self.empty1) ==6 and len(self.empty2) < 6 :
                    self.empty2.append(23)
                    self.num_entry2.insert(END, '23 ')
                    self.btn_23.config(state='disable')

            elif len(self.empty2) == 6 and len(self.empty3) < 6:
                self.empty3.append(23)
                self.num_entry3.insert(END, '23 ')
                self.btn_23.config(state='disable')
            else:
                messagebox.showinfo(title=None, message="Exceeded")

        def twenty_4(self):
            from tkinter import messagebox

            if len(self.empty1) < 6:
                    self.empty1.append(24)
                    self.num_entry1.insert(END, '24 ')
                    self.btn_24.config(state='disable')

            elif  len(self.empty1) ==6 and len(self.empty2) < 6 :
                    self.empty2.append(24)
                    self.num_entry2.insert(END,'24 ')
                    self.btn_24.config(state='disable')

            elif len(self.empty2) == 6 and len(self.empty3) < 6:
                self.empty3.append(24)
                self.num_entry3.insert(END,'24 ')
                self.btn_24.config(state='disable')
            else:
                messagebox.showinfo(title=None, message="Exceeded")

        def twenty_5(self):
            from tkinter import messagebox

            if len(self.empty1) < 6:
                    self.empty1.append(25)
                    self.num_entry1.insert(END,'25 ')
                    self.btn_25.config(state='disable')

            elif  len(self.empty1) ==6 and len(self.empty2) < 6 :
                    self.empty2.append(25)
                    self.num_entry2.insert(END,'25 ')
                    self.btn_25.config(state='disable')

            elif len(self.empty2) == 6 and len(self.empty3) < 6:
                self.empty3.append(25)
                self.num_entry3.insert(END,'25 ')
                self.btn_25.config(state = 'disable')
            else:
                messagebox.showinfo(title=None, message="Exceeded")

        def twenty_6(self):
            from tkinter import messagebox

            if len(self.empty1) < 6:
                    self.empty1.append(26)
                    self.num_entry1.insert(END,'26 ')
                    self.btn_26.config(state='disable')

            elif  len(self.empty1) ==6 and len(self.empty2) < 6 :
                    self.empty2.append(26)
                    self.num_entry2.insert(END, '26 ')
                    self.btn_26.config(state='disable')

            elif len(self.empty2) == 6 and len(self.empty3) < 6:
                self.empty3.append(26)
                self.num_entry3.insert(END,'26 ')
                self.btn_26.config(state='disable')
            else:
                messagebox.showinfo(title=None, message="Exceeded")

        def twenty_7(self):
            from tkinter import messagebox

            if len(self.empty1) < 6:
                    self.empty1.append(27)
                    self.num_entry1.insert(END, '27 ')
                    self.btn_27.config(state='disable')

            elif  len(self.empty1) ==6 and len(self.empty2) < 6 :
                    self.empty2.append(27)
                    self.num_entry2.insert(END, '27 ')
                    self.btn_27.config(state='disable')

            elif len(self.empty2) == 6 and len(self.empty3) < 6:
                self.empty3.append(27)
                self.num_entry3.insert(END,'27 ')
                self.btn_27.config(state='disable')
            else:
                messagebox.showinfo(title=None, message="Exceeded")

        def twenty_8(self):
            from tkinter import messagebox

            if len(self.empty1) < 6:
                    self.empty1.append(28)
                    self.num_entry1.insert(END, '28 ')
                    self.btn_28.config(state='disable')

            elif  len(self.empty1) ==6 and len(self.empty2) < 6 :
                    self.empty2.append(28)
                    self.num_entry2.insert(END,'28 ')
                    self.btn_28.config(state='disable')

            elif len(self.empty2) == 6 and len(self.empty3) < 6:
                self.empty3.append(28)
                self.num_entry3.insert(END,'28 ')
                self.btn_28.config(state='disable')
            else:
                messagebox.showinfo(title=None, message="Exceeded")

        def twenty_9(self):
            from tkinter import messagebox

            if len(self.empty1) < 6:
                    self.empty1.append(29)
                    self.num_entry1.insert(END,'29 ')
                    self.btn_29.config(state='disable')

            elif  len(self.empty1) ==6 and len(self.empty2) < 6 :
                    self.empty2.append(29)
                    self.num_entry2.insert(END,'29 ')
                    self.btn_29.config(state='disable')

            elif len(self.empty2) == 6 and len(self.empty3) < 6:
                self.empty3.append(29)
                self.num_entry3.insert(END, '29 ')
                self.btn_29.config(state='disable')
            else:
                messagebox.showinfo(title=None, message="Exceeded")

        def thirty(self):
            from tkinter import messagebox

            if len(self.empty1) < 6:
                    self.empty1.append(30)
                    self.num_entry1.insert(END, '30 ')
                    self.btn_30.config(state='disable')

            elif  len(self.empty1) ==6 and len(self.empty2) < 6 :
                    self.empty2.append(30)
                    self.num_entry2.insert(END, '30 ')
                    self.btn_30.config(state='disable')

            elif len(self.empty2) == 6 and len(self.empty3) < 6:
                self.empty3.append(30)
                self.num_entry3.insert(END,'30 ')
                self.btn_30.config(state='disable')
            else:
                messagebox.showinfo(title=None, message="Exceeded")


        def thirty_1(self):
            from tkinter import messagebox

            if len(self.empty1) < 6:
                    self.empty1.append(31)
                    self.num_entry1.insert(END,'31 ')
                    self.btn_31.config(state='disable')

            elif  len(self.empty1) ==6 and len(self.empty2) < 6 :
                    self.empty2.append(31)
                    self.num_entry2.insert(END,'31 ')
                    self.btn_31.config(state='disable')

            elif len(self.empty2) == 6 and len(self.empty3) < 6:
                self.empty3.append(31)
                self.num_entry3.insert(END,'31 ')
                self.btn_31.config(state='disable')
            else:
                messagebox.showinfo(title=None, message="Exceeded")

        def thirty_2(self):
            from tkinter import messagebox

            if len(self.empty1) < 6:
                    self.empty1.append(32)
                    self.num_entry1.insert(END,'32 ')
                    self.btn_32.config(state='disable')

            elif  len(self.empty1) ==6 and len(self.empty2) < 6 :
                    self.empty2.append(32)
                    self.num_entry2.insert(END,'32 ')
                    self.btn_32.config(state='disable')

            elif len(self.empty2) == 6 and len(self.empty3) < 6:
                self.empty3.append(32)
                self.num_entry3.insert(END,'32 ')
                self.btn_32.config(state='disable')
            else:
                messagebox.showinfo(title=None, message="Exceeded")

        def thirty_3(self):
            from tkinter import messagebox

            if len(self.empty1) < 6:
                    self.empty1.append(33)
                    self.num_entry1.insert(END,'33 ')
                    self.btn_33.config(state='disable')

            elif  len(self.empty1) ==6 and len(self.empty2) < 6 :
                    self.empty2.append(33)
                    self.num_entry2.insert(END,'33 ')
                    self.btn_33.config(state='disable')

            elif len(self.empty2) == 6 and len(self.empty3) < 6:
                self.empty3.append(33)
                self.num_entry3.insert(END,'33 ')
                self.btn_33.config(state='disable')
            else:
                messagebox.showinfo(title=None, message="Exceeded")

        def thirty_4(self):
            from tkinter import messagebox

            if len(self.empty1) < 6:
                    self.empty1.append(34)
                    self.num_entry1.insert(END,'34 ')
                    self.btn_34.config(state='disable')

            elif  len(self.empty1) ==6 and len(self.empty2) < 6 :
                    self.empty2.append(34)
                    self.num_entry2.insert(END,'34 ')
                    self.btn_34.config(state='disable')

            elif len(self.empty2) == 6 and len(self.empty3) < 6:
                self.empty3.append(34)
                self.num_entry3.insert(END,'34')
                self.btn_34.config(state='disable')
            else:
                messagebox.showinfo(title=None, message="Exceeded")

        def thirty_5(self):
            from tkinter import messagebox

            if len(self.empty1) < 6:
                    self.empty1.append(35)
                    self.btn_35.config(state='disable')

            elif  len(self.empty1) ==6 and len(self.empty2) < 6 :
                    self.empty2.append(35)
                    self.btn_35.config(state='disable')

            elif len(self.empty2) == 6 and len(self.empty3) < 6:
                self.empty3.append(35)
                self.btn_35.config(state='disable')
            else:
                messagebox.showinfo(title=None, message="Exceeded")

        def thirty_6(self):
            from tkinter import messagebox

            if len(self.empty1) < 6:
                    self.empty1.append(36)
                    self.btn_36.config(state='disable')

            elif  len(self.empty1) ==6 and len(self.empty2) < 6 :
                    self.empty2.append(36)
                    self.btn_36.config(state='disable')

            elif len(self.empty2) == 6 and len(self.empty3) < 6:
                self.empty3.append(36)
                self.btn_36.config(state='disable')
            else:
                messagebox.showinfo(title=None, message="Exceeded")

        def thirty_7(self):
            from tkinter import messagebox

            if len(self.empty1) < 6:
                    self.empty1.append(37)
                    self.btn_37.config(state='disable')

            elif  len(self.empty1) ==6 and len(self.empty2) < 6 :
                    self.empty2.append(37)
                    self.btn_37.config(state='disable')

            elif len(self.empty2) == 6 and len(self.empty3) < 6:
                self.empty3.append(37)
                self.btn_37.config(state='disable')
            else:
                messagebox.showinfo(title=None, message="Exceeded")

        def thirty_8(self):
            from tkinter import messagebox

            if len(self.empty1) < 6:
                    self.empty1.append(38)
                    self.btn_38.config(state='disable')

            elif  len(self.empty1) ==6 and len(self.empty2) < 6 :
                    self.empty2.append(38)
                    self.btn_1.config(state='disable')

            elif len(self.empty2) == 6 and len(self.empty3) < 6:
                self.empty3.append(38)
                self.btn_1.config(state='disable')
            else:
                messagebox.showinfo(title=None, message="Exceeded")

        def thirty_9(self):
            from tkinter import messagebox

            if len(self.empty1) < 6:
                    self.empty1.append(39)
                    self.btn_39.config(state='disable')

            elif  len(self.empty1) ==6 and len(self.empty2) < 6 :
                    self.empty2.append(39)
                    self.btn_39.config(state='disable')

            elif len(self.empty2) == 6 and len(self.empty3) < 6:
                self.empty3.append(39)
                self.btn_39.config(state='disable')
            else:
                messagebox.showinfo(title=None, message="Exceeded")

        def fourty(self):
            from tkinter import messagebox

            if len(self.empty1) < 6:
                    self.empty1.append(40)
                    self.btn_40.config(state='disable')

            elif  len(self.empty1) ==6 and len(self.empty2) < 6 :
                    self.empty2.append(40)
                    self.btn_40.config(state='disable')

            elif len(self.empty2) == 6 and len(self.empty3) < 6:
                self.empty3.append(40)
                self.btn_40.config(state='disable')
            else:
                messagebox.showinfo(title=None, message="Exceeded")

        def fourty_1(self):
            from tkinter import messagebox

            if len(self.empty1) < 6:
                    self.empty1.append(41)
                    self.btn_41.config(state='disable')

            elif  len(self.empty1) ==6 and len(self.empty2) < 6 :
                    self.empty2.append(41)
                    self.btn_41.config(state='disable')

            elif len(self.empty2) == 6 and len(self.empty3) < 6:
                self.empty3.append(41)
                self.btn_41.config(state='disable')
            else:
                messagebox.showinfo(title=None, message="Exceeded")

        def fourty_2(self):
            from tkinter import messagebox

            if len(self.empty1) < 6:
                    self.empty1.append(42)
                    self.btn_42.config(state='disable')

            elif  len(self.empty1) ==6 and len(self.empty2) < 6 :
                    self.empty2.append(42)
                    self.btn_42.config(state='disable')

            elif len(self.empty2) == 6 and len(self.empty3) < 6:
                self.empty3.append(42)
                self.btn_42.config(state='disable')
            else:
                messagebox.showinfo(title=None, message="Exceeded")

        def fourty_3(self):
            from tkinter import messagebox

            if len(self.empty1) < 6:
                    self.empty1.append(43)
                    self.btn_43.config(state='disable')

            elif  len(self.empty1) ==6 and len(self.empty2) < 6 :
                    self.empty2.append(43)
                    self.btn_43.config(state='disable')

            elif len(self.empty2) == 6 and len(self.empty3) < 6:
                self.empty3.append(43)
                self.btn_43.config(state='disable')
            else:
                messagebox.showinfo(title=None, message="Exceeded")

        def fourty_4(self):
            from tkinter import messagebox

            if len(self.empty1) < 6:
                    self.empty1.append(44)
                    self.btn_44.config(state='disable')

            elif  len(self.empty1) ==6 and len(self.empty2) < 6 :
                    self.empty2.append(44)
                    self.btn_44.config(state='disable')

            elif len(self.empty2) == 6 and len(self.empty3) < 6:
                self.empty3.append(44)
                self.btn_44.config(state='disable')
            else:
                messagebox.showinfo(title=None, message="Exceeded")


        def fourty_5(self):
            from tkinter import messagebox

            if len(self.empty1) < 6:
                    self.empty1.append(45)
                    self.btn_45.config(state='disable')

            elif  len(self.empty1) ==6 and len(self.empty2) < 6 :
                    self.empty2.append(45)
                    self.btn_45.config(state='disable')

            elif len(self.empty2) == 6 and len(self.empty3) < 6:
                self.empty3.append(45)
                self.btn_45.config(state='disable')
            else:
                messagebox.showinfo(title=None, message="Exceeded")

        def fourty_6(self):
            from tkinter import messagebox

            if len(self.empty1) < 6:
                    self.empty1.append(46)
                    self.btn_46.config(state='disable')

            elif  len(self.empty1) ==6 and len(self.empty2) < 6 :
                    self.empty2.append(46)
                    self.btn_46.config(state='disable')

            elif len(self.empty2) == 6 and len(self.empty3) < 6:
                self.empty3.append(46)
                self.btn_46.config(state='disable')
            else:
                messagebox.showinfo(title=None, message="Exceeded")

        def fourty_7(self):
            from tkinter import messagebox

            if len(self.empty1) < 6:
                    self.empty1.append(47)
                    self.btn_47.config(state='disable')

            elif  len(self.empty1) ==6 and len(self.empty2) < 6 :
                    self.empty2.append(47)
                    self.btn_47.config(state='disable')

            elif len(self.empty2) == 6 and len(self.empty3) < 6:
                self.empty3.append(47)
                self.btn_47.config(state='disable')
            else:
                messagebox.showinfo(title=None, message="Exceeded")

        def fourty_8(self):
            from tkinter import messagebox

            if len(self.empty1) < 6:
                    self.empty1.append(48)
                    self.btn_48.config(state='disable')

            elif  len(self.empty1) ==6 and len(self.empty2) < 6 :
                    self.empty2.append(48)
                    self.btn_48.config(state='disable')

            elif len(self.empty2) == 6 and len(self.empty3) < 6:
                self.empty3.append(48)
                self.btn_48.config(state='disable')
            else:
                messagebox.showinfo(title=None, message="Exceeded")

        def fourty_9(self):
            from tkinter import messagebox

            if len(self.empty1) < 6:
                    pick = self.empty1.append(49)
                    self.btn_49.config(state='disable')

            elif  len(self.empty1) ==6 and len(self.empty2) < 6 :
                    self.empty2.append(49)
                    self.btn_49.config(state='disable')

            elif len(self.empty2) == 6 and len(self.empty3) < 6:
                self.empty3.append(49)
                self.btn_49.config(state='disable')
            else:
                messagebox.showinfo(title=None, message="Exceeded")


        #play function
        def play(self):

            if len(self.empty1) == 6 and len(self.empty1) !=0:
                for i in self.game_numbers:
                    if i in self.empty1:
                        self.compare.append(i)
                for i in self.dict:
                    if i == len(self.compare):
                        self.wins_entry1.insert(0,self.dict[i])

                self.results_entry1.insert(0, self.compare)
                self.draw_entry1.insert(0, self.game_numbers)
                self.match_entry1.insert(0,len(self.compare))
                self.num_entry1.config(state='readonly')
                self.results_entry1.config(state='readonly')
                self.draw_entry1.config(state='readonly')
                f = open("details.txt", "a")
                f.write(("Numbers you played for set1: " + self.num_entry1.get()))
                f.write("Lotto numbers for set1: " + self.draw_entry1.get())
                f.write(" Winning numbers for set1: " + " " + self.draw_entry1.get())
                f.write("matching numbers for set1: " + " " + self.match_entry1.get())
                f.write("Your money for set1: " +" " + self.wins_entry1.get())
                f.close()


                if len(self.empty2) == 6 and len(self.empty2) !=0:
                    self.compare.clear()
                    for i in self.game_numbers:
                        if i in self.empty2:
                            self.compare.append(i)
                    for i in self.dict:
                        if i == len(self.compare):
                            self.wins_entry2.insert(0, self.dict[i])

                    self.results_entry2.insert(0, self.compare)
                    self.draw_entry2.insert(0, self.game_numbers)
                    self.match_entry2.insert(0,len(self.compare))
                    self.num_entry2.config(state='readonly')
                    self.results_entry2.config(state='readonly')
                    self.draw_entry2.config(state='readonly')
                    f = open("details.txt", "a")
                    f.write(("Numbers you played for set2: " + self.num_entry2.get()))
                    f.write("Lotto numbers for set2: " + self.draw_entry2.get())
                    f.write(" Winning numbers for set2: " + " " + self.draw_entry2.get())
                    f.write("matching numbers for set2: " + " " + self.match_entry2.get())
                    f.write("Your money for set2: " + " " + self.wins_entry2.get())
                    f.close()


                    if len(self.empty3) == 6 and len(self.empty3) !=0:
                        self.compare.clear()
                        for i in self.game_numbers:
                            if i in self.empty3:
                                self.compare.append(i)
                        for i in self.dict:
                            if i == len(self.compare):
                                self.wins_entry3.insert(0, self.dict[i])
                        self.results_entry3.insert(0, self.compare)
                        self.draw_entry3.insert(0, self.game_numbers)
                        self.match_entry3.insert(0,len(self.compare))
                        self.num_entry3.config(state='readonly')
                        self.results_entry3.config(state='readonly')
                        self.draw_entry3.config(state='readonly')
                        f = open("details.txt", "a")
                        f.write(("Numbers you played for set3: " + self.num_entry3.get()))
                        f.write("Lotto numbers for set3: " + self.draw_entry3.get())
                        f.write(" Winning numbers for set3: " + " " + self.draw_entry3.get())
                        f.write("matching numbers for set3: " + " " + self.match_entry3.get())
                        f.write("Your money for set3: " + " " + self.wins_entry3.get())
                        f.close()
                    #total = float(self.wins_entry1.get()) + float(self.wins_entry2.get()) + float(self.wins_entry3.get())
                    #self.total_entry.insert(0,total)




        def clear(self):
            self.num_entry1.config(state='normal')
            self.results_entry1.config(state='normal')
            self.draw_entry1.config(state='normal')

            self.num_entry2.config(state='normal')
            self.results_entry2.config(state='normal')
            self.draw_entry2.config(state='normal')

            self.num_entry3.config(state='normal')
            self.results_entry3.config(state='normal')
            self.draw_entry3.config(state='normal')

            self.results_entry1.delete(0,END)
            self.draw_entry1.delete(0,END)
            self.num_entry1.delete(0,END)

            self.results_entry2.delete(0,END)
            self.draw_entry2.delete(0,END)
            self.num_entry2.delete(0,END)

            self.results_entry3.delete(0,END)
            self.draw_entry3.delete(0,END)
            self.num_entry3.delete(0,END)

            self.btn_1.config(state='normal')
            self.btn_2.config(state='normal')
            self.btn_3.config(state='normal')
            self.btn_4.config(state='normal')
            self.btn_5.config(state='normal')
            self.btn_6.config(state='normal')
            self.btn_7.config(state='normal')
            self.btn_8.config(state='normal')
            self.btn_9.config(state='normal')
            self.btn_10.config(state='normal')
            self.btn_11.config(state='normal')
            self.btn_12.config(state='normal')
            self.btn_13.config(state='normal')
            self.btn_14.config(state='normal')
            self.btn_15.config(state='normal')
            self.btn_16.config(state='normal')
            self.btn_17.config(state='normal')
            self.btn_18.config(state='normal')
            self.btn_19.config(state='normal')
            self.btn_20.config(state='normal')
            self.btn_21.config(state='normal')
            self.btn_22.config(state='normal')
            self.btn_23.config(state='normal')
            self.btn_24.config(state='normal')
            self.btn_25.config(state='normal')
            self.btn_26.config(state='normal')
            self.btn_27.config(state='normal')
            self.btn_28.config(state='normal')
            self.btn_29.config(state='normal')
            self.btn_30.config(state='normal')
            self.btn_31.config(state='normal')
            self.btn_32.config(state='normal')
            self.btn_33.config(state='normal')
            self.btn_34.config(state='normal')
            self.btn_35.config(state='normal')
            self.btn_36.config(state='normal')
            self.btn_37.config(state='normal')
            self.btn_38.config(state='normal')
            self.btn_39.config(state='normal')
            self.btn_40.config(state='normal')
            self.btn_41.config(state='normal')
            self.btn_42.config(state='normal')
            self.btn_43.config(state='normal')
            self.btn_44.config(state='normal')
            self.btn_45.config(state='normal')
            self.btn_46.config(state='normal')
            self.btn_47.config(state='normal')
            self.btn_48.config(state='normal')
            self.btn_49.config(state='normal')

            self.empty1.clear()
            self.empty2.clear()
            self.empty3.clear()
            self.compare.clear()


        def claim(self):
            if self.wins_entry1.get() == "0" and self.wins_entry2.get() == "0" and self.wins_entry3.get() == "0":
                messagebox.showwarning(title="Lost!", message="Sorry you have not won, please play again.")
            else:
                messagebox.showinfo(title="Congragulations", message="Congragulations! You win!")
                import claim_prize
                root.destroy()











y=Lotto_machine(root)
root.mainloop()
