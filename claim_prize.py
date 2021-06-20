from tkinter import *
from tkinter import  ttk
from tkinter import messagebox
from login import Get

root = Tk()
root.geometry("800x800")

class Prize_claim():
    from tkinter import ttk
    def __init__(self,master):
        self.bank_label = Label(master, text= "Bank")
        self.bank_label.place(x=20,y=40)

        self.banks_list = ttk.Combobox(master, text="Choose a bank.")
        self.banks_list['values'] = ('ABSA','FNB','CAPITEC','STANDARD BANK')
        self.banks_list.current()
        self.banks_list.place(x=100,y=40)

        self.winner_name_label=Label(master, text="Name:")
        self.winner_name_label.place(x=20, y=100)
        self.winner_name_entry = Entry(master)
        self.winner_name_entry.place(x=100,y=100)

        self.surname_label = Label(master, text="Surname")
        self.surname_label.place(x=20,y=150)
        self.surname_entry = Entry(master)
        self.surname_entry.place(x=100,y=150)

        self.emaiil_label = Label(master, text="email")
        self.emaiil_label.place(x=20,y=200)
        self.email_entry = Entry(master)
        self.email_entry.place(x=100,y=200)

        self.claim_btn = Button(master, text ="SEND", command = self.emailer)
        self.claim_btn.place(x=40, y=250)

    def emailer(self):
        import smtplib
        from email.mime.text import MIMEText
        from email.mime.multipart import MIMEMultipart

        x = Get.name1(self)
        sender_email_id = 'stuurmanmzwandile@gmail.com'
        receiver_email_id = ['sithandathuzipho@gmail.com', self.email_entry.insert(0,x)]
        password = input("Enter your password: ")
        subject = "Your winnings."
        msg = MIMEMultipart()
        msg['From'] = sender_email_id
        msg['To'] = ', ' .join(receiver_email_id)
        msg['Subject'] = subject
        body = "Your name:" + self.winner_name_entry.get() + " " + "Your Surname:" + self.surname_entry.get() + "Your Bank is:" + self.banks_list.get()
        msg.attach(MIMEText(body, 'plain'))

        text = msg.as_string()
        s = smtplib.SMTP('smtp.gmail.com', 587)
        # start TLS for security
        s.starttls()
        # Authentication

        s.login(sender_email_id, password)
        # message to be sent

        # sending the mail
        s.sendmail(sender_email_id, receiver_email_id, text)
        # terminating the session
        s.quit()








y=Prize_claim(root)
root.mainloop()


