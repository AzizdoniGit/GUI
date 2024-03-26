from tkinter import *
from datetime import datetime

root = Tk()
root.title('Digital Clock (Sam)')
root.geometry('600x200+500+280')
root.resizable(False, False)
root.config(bg='black', pady=40)

text1 = Label(root, text='Hello world',
               font=('Bahnschrift Light', 45, 'bold'),
               fg='white', bg='black')

text2 = Label(root, text='',
               font=('Bahnschrift Light', 9, ''),
               fg='gray', bg='black', pady=10)

text3 = Label(root, text='',
               font=('Bahnschrift Light', 9, ''),
               fg='gray', bg='black', pady=10)

text4 = Label(root, text='',
               font=('Bahnschrift Light', 9, ''),
               fg='gray', bg='black', pady=10)

text5 = Label(root, text='',
               font=('Bahnschrift Light', 9, ''),
               fg='gray', bg='black', pady=10)





def clock():
    now = datetime.now()
    now = now.strftime('%a %H : %M : %S ')
    text1.config(text=now)
    text2.config(text="HOURS")
    text3.config(text="MINUTES")
    text4.config(text="SECONDS")
    text5.config(text="DAY")
    text5.place(x=120, y=70)
    text2.place(x=210, y=70)
    text3.place(x=326, y=70)
    text4.place(x=435, y=70)
    root.after(1000, clock)

text1.pack()
text2.pack()
text3.pack()
text4.pack()
clock()
root.mainloop()


