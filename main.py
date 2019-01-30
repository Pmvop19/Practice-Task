from tkinter import *
import solve


def button_clicked(event):  # функция, страбатываемая при нажатии левой клавиши мышки, считывает  
    s = int(entry1.get())   # значения и вызывает срабатывание функции размена из файла solve.py.
    a = int(entry2.get())
    b = int(entry3.get())
    x = int(entry4.get())
    an, bn = solve.solve(s, a, b, x)
    label5['text'] = 'An='+str(an)
    label6['text'] = 'Bn='+str(bn)


root = Tk()
root.title("Размен")
root.resizable(False, False) # Запрет скалирования окна по осям X и Y

label1 = Label(root, text='S', width=5, font=15)
label2 = Label(root, text='A', width=5, font=15)
label3 = Label(root, text='B', width=5, font=15)
label4 = Label(root, text='X', width=5, font=15)

entry1 = Entry(root, width=5, font=15) 
entry2 = Entry(root, width=5, font=15)
entry3 = Entry(root, width=5, font=15)
entry4 = Entry(root, width=5, font=15)

label1.grid(row=0, column=0)
label2.grid(row=1, column=0)
label3.grid(row=2, column=0)
label4.grid(row=3, column=0)

entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)
entry3.grid(row=2, column=1)
entry4.grid(row=3, column=1)

button1 = Button(root,width=10, text="Разменять")
button1.grid(columnspan=2, row=4)

label5 = Label(root, width=5, font=15)
label6 = Label(root, width=5, font=15)
label5.grid(column=0, row=5)
label6.grid(column=1, row=5)

button1.bind("<Button-1>", button_clicked)


root.mainloop()
