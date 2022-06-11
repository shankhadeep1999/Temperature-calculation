from  tkinter import *

frist_num = None
oprator = None

def get_digit(digit):
    current = result_lable['text']
    new = current + str(digit)
    result_lable.config(text=new)

def clear():
    result_lable.config(text="")

def get_oprator(op):
    global  frist_num,oprator

    frist_num = int(result_lable['text'])
    oprator = op
    result_lable.config(text='')

    # Find result

    far = (frist_num) * 9 / 5 + 32
    cels = (frist_num) * 9 / 5 + 32

    if oprator == 'F':
        result_lable.config(text=str(far))
    elif oprator == 'C':
        result_lable.config(text=str(cels))


root = Tk()
root.title("Temperature calculation")
root.geometry('280x310')
root.resizable(0,0)
root.configure(background="black")

result_lable = Label(root,text='',bg="black",fg="white")
result_lable.grid(row=0,column=0,columnspan=5,pady=(45,25),sticky='w')
result_lable.config(font=('verdana',30,'bold'))

bt7 = Button(root,text='7',bg='#00a65a',fg="White",width=5,height=2,command=lambda :get_digit(7))
bt7.grid(row="1",column=0)
bt7.config(font=('vardana',14,'bold'))

bt8 = Button(root,text="8",bg='#00a65a',fg="White",width=5,height=2,command=lambda :get_digit(8))
bt8.grid(row="1",column=1)
bt8.config(font=('vardana',14,'bold'))

bt9 = Button(root,text="9",bg='#00a65a',fg="White",width=5,height=2,command=lambda :get_digit(9))
bt9.grid(row="1",column=2)
bt9.config(font=('vardana',14,'bold'))

bt_cl = Button(root,text="AC",bg='#00a65a',fg="White",width=5,height=2,command=lambda :clear())
bt_cl.grid(row="1",column=3)
bt_cl.config(font=('vardana',14,'bold'))


bt4 = Button(root,text="4",bg='#00a65a',fg="White",width=5,height=2,command=lambda :get_digit(4))
bt4.grid(row="2",column=0)
bt4.config(font=('vardana',14,'bold'))

bt5 = Button(root,text="5",bg='#00a65a',fg="White",width=5,height=2,command=lambda :get_digit(5))
bt5.grid(row="2",column=1)
bt5.config(font=('vardana',14,'bold'))

bt6 = Button(root,text="6",bg='#00a65a',fg="White",width=5,height=2,command=lambda :get_digit(6))
bt6.grid(row="2",column=2)
bt6.config(font=('vardana',14,'bold'))

bt3 = Button(root,text="3",bg='#00a65a',fg="White",width=5,height=2,command=lambda :get_digit(3))
bt3.grid(row="2",column=3)
bt3.config(font=('vardana',14,'bold'))

bt2 = Button(root,text="2",bg='#00a65a',fg="White",width=5,height=2,command=lambda :get_digit(2))
bt2.grid(row="3",column=0)
bt2.config(font=('vardana',14,'bold'))

bt1 = Button(root,text="1",bg='#00a65a',fg="White",width=5,height=2,command=lambda :get_digit(1))
bt1.grid(row="3",column=1)
bt1.config(font=('vardana',14,'bold'))

btF = Button(root,text="F",bg='#00a65a',fg="White",width=5,height=2,command=lambda :get_oprator("F"))
btF.grid(row="3",column=2)
btF.config(font=('vardana',14,'bold'))

btC = Button(root,text="C",bg='#00a65a',fg="White",width=5,height=2,command=lambda :get_oprator("F"))
btC.grid(row="3",column=3)
btC.config(font=('vardana',14,'bold'))



root.mainloop()
