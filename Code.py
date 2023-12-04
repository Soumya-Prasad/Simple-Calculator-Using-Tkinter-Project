from tkinter import*
window=Tk()
window.title("Calculator")
window.geometry("260x245")
window.resizable(False,False)
window.iconbitmap("./calcu.ico")
window.configure(bg="#2F0909")
text=StringVar()
e=Entry(window,font="Arial 28",width=7,bd=6,bg="#FAF0DD",textvariable=text,justify=RIGHT).grid(columnspan=5,ipadx=45)
def btn_click(item):
    global expression
    expression = expression + str(item)
    text.set(expression)
def bt_clear():
    global expression
    expression = ""
    text.set("")
def bt_equal():
    global expression
    result=str(eval(expression))
    text.set(result)
    expression=""
expression=""
b1=Button(window,text="7",bd=4,height=2,width=7,bg="#FFCBA4",fg="black",command=lambda:btn_click(7)).grid(row=1,column=0,padx=1,pady=1)
b2=Button(window,text="8",bd=4,height=2,width=7,bg="#FFCBA4",fg="black",command=lambda:btn_click(8)).grid(row=1,column=1,padx=1,pady=1)
b3=Button(window,text="9",bd=4,height=2,width=7,bg="#FFCBA4",fg="black",command=lambda:btn_click(9)).grid(row=1,column=2,padx=1,pady=1)
b4=Button(window,text="/",bd=4,height=2,width=7,bg="#FFCBA4",fg="black",command=lambda:btn_click("/")).grid(row=1,column=3,padx=1,pady=1)
b5=Button(window,text="4",bd=4,height=2,width=7,bg="#FFCBA4",fg="black",command=lambda:btn_click(4)).grid(row=2,column=0,padx=1,pady=1)
b6=Button(window,text="5",bd=4,height=2,width=7,bg="#FFCBA4",fg="black",command=lambda:btn_click(5)).grid(row=2,column=1,padx=1,pady=1)
b7=Button(window,text="6",bd=4,height=2,width=7,bg="#FFCBA4",fg="black",command=lambda:btn_click(6)).grid(row=2,column=2,padx=1,pady=1)
b8=Button(window,text="*",bd=4,height=2,width=7,bg="#FFCBA4",fg="black",command=lambda:btn_click("*")).grid(row=2,column=3,padx=1,pady=1)
b9=Button(window,text="1",bd=4,height=2,width=7,bg="#FFCBA4",fg="black",command=lambda:btn_click(1)).grid(row=3,column=0,padx=1,pady=1)
b10=Button(window,text="2",bd=4,height=2,width=7,bg="#FFCBA4",fg="black",command=lambda:btn_click(2)).grid(row=3,column=1,padx=1,pady=1)
b11=Button(window,text="3",bd=4,height=2,width=7,bg="#FFCBA4",fg="black",command=lambda:btn_click(3)).grid(row=3,column=2,padx=1,pady=1)
b12=Button(window,text="+",bd=4,height=2,width=7,bg="#FFCBA4",fg="black",command=lambda:btn_click("+")).grid(row=3,column=3,padx=1,pady=1)
b13=Button(window,text="c",bd=4,height=2,width=7,bg="#FFCBA4",fg="black",command=lambda:bt_clear()).grid(row=4,column=0,padx=1,pady=1)
b14=Button(window,text="0",bd=4,height=2,width=7,bg="#FFCBA4",fg="black",command=lambda:btn_click(0)).grid(row=4,column=1,padx=1,pady=1)
b15=Button(window,text="=",bd=4,height=2,width=7,bg="#FFCBA4",fg="black",command=lambda:bt_equal()).grid(row=4,column=2,padx=1,pady=1)
b16=Button(window,text="-",bd=4,height=2,width=7,bg="#FFCBA4",fg="black",command=lambda:btn_click("-")).grid(row=4,column=3,padx=1,pady=1)
window.mainloop()