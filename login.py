from tkinter import *
from tkinter import messagebox
root = Tk()
root.title("Login")
root.geometry("500x500")

root.config(bg="dark slate grey")

class Login():

    def __init__(self,master):
        #Name and Surname labels and entries
        self.name_label = Label(master, text="Enter your name")
        self.name_label.place(x=10,y=10)
        self.surname_label = Label(master, text="Enter Surname")
        self.surname_label.place(x=10,y=50)
        self.name_entry= Entry(master)
        self.name_entry.place(x=150,y=10)
        self.surname_entry = Entry(master)
        self.surname_entry.place(x=150,y=50)

        self.email_label = Label(master, text="Enter your email: ")
        self.email_label.place(x=10, y=100)
        self.email_entry = Entry(master)
        self.email_entry.place(x=150,y=100)



        self.id_entry = Entry(master)
        self.id_entry.config(state='readonly')
        self.id_entry.place(x=200,y=150)

        self.email_validator = Button(root, text="Enter Id number: ", command=self.details)
        self.email_validator.place(x=10, y=150)

        self.login_btn = Button(root, text ="login", command=self.id_check)
        self.login_btn.place(x=10, y=250)



    def details(self):
        name = self.name_entry.get()
        surname = self.surname_entry.get()
        email = str(self.email_entry.get())


        if "@" in self.email_entry.get():
            self.id_entry.config(state='normal')

        else:
            messagebox.showinfo(title='Alert!', message="Please enter valid email adress!")
            self.id_entry.config(state='readonly')
            self.email_entry.delete(0,END)

    def id_check(self):
        try:
            Id = int(self.id_entry.get())
            id_ls = self.id_entry.get()

            year = self.id_entry.get()[1]
            year2 = self.id_entry.get()[0:2]

            if type(Id) == type(str()) or len(id_ls) != 13:
                raise ValueError
            elif int(year) <= 3:

                messagebox.showinfo(title="Play!", message="Lets Play!")
                import lotto
                root.destroy()
            elif int(year2) >3 and int(year2) > 21:
                messagebox.showinfo(title="Play!", message="Lets Play!")
                import lotto
                root.destroy()
            else:
                #x = int(year) -3
                messagebox.showinfo(title="Under Age", message="Your are too young to play")
        except ValueError:

            messagebox.showerror(title="Invalid Id", message="Please enter valid ID")
            self.id_entry.delete(0,END)



x=Login(root)
root.mainloop()

