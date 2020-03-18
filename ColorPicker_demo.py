from tkinter import*


window = Tk()
window.title("Homework")
window.config(bg="gray")
window.minsize(400,350)
window.maxsize(400,350)

btn1 = Button()
btn1.config(width=10,bg="#7fff00",)
btn1.place(x=170, y=20)

btn2 = Button()
btn2.config(width=10,bg="#ee7621")
btn2.place(x=170,y=45)

btn3 = Button()
btn3.config(width=10,bg="#ff7f50")
btn3.place(x=170, y=70)

btn4 = Button()
btn4.config(width=10,bg="#00ffff")
btn4.place(x=170,y=95)

btn5 = Button()
btn5.config(width=10,bg="#8b8878")
btn5.place(x=170, y=120)

btn6 = Button()
btn6.config(width=10,bg="#006400")
btn6.place(x=170,y=145)

btn7 = Button()
btn7.config(width=10,bg="#bdb76b")
btn7.place(x=170, y=170)

btn8 = Button()
btn8.config(width=10,bg="#ff8c00")
btn8.place(x=170,y=195)

btn9 = Button()
btn9.config(width=10,bg="#9932cc")
btn9.place(x=170, y=220)

btn10 = Button()
btn10.config(width=10,bg="#8fbc8f")
btn10.place(x=170,y=245)

btn11 = Button()
btn11.config(width=10,text="close",bg="gray",command = lambda window=window:quit(window))
btn11.place(x=170,y=270)

lbl1 = Label()
lbl1.config(text="chartreuse1",bg="gray")
lbl1.place(x=80,y=20)

lbl2 = Label()
lbl2.config(text="chocolate2",bg="gray")
lbl2.place(x=80,y=45)

lbl3 = Label()
lbl3.config(text="coral",bg="gray")
lbl3.place(x=80,y=70)

lbl4 = Label()
lbl4.config(text="cyan1",bg="gray")
lbl4.place(x=80,y=95)

lbl5 = Label()
lbl5.config(text="cornsilk4",bg="gray")
lbl5.place(x=80,y=120)

lbl6 = Label()
lbl6.config(text="DarkGreen",bg="gray")
lbl6.place(x=80,y=145)

lbl7 = Label()
lbl7.config(text="DarkKhaki",bg="gray")
lbl7.place(x=80,y=170)

lbl8 = Label()
lbl8.config(text="DarkOrange",bg="gray")
lbl8.place(x=80,y=195)

lbl9 = Label()
lbl9.config(text="DarkOrchid",bg="gray")
lbl9.place(x=80,y=220)

lbl10 = Label()
lbl10.config(text="DarkSeaGreen",bg="gray")
lbl10.place(x=80,y=245)

lbl11 = Label()
lbl11.config(text="#7fff00",bg="gray")
lbl11.place(x=270,y=20)

lbl12 = Label()
lbl12.config(text="#ee7621",bg="gray")
lbl12.place(x=270,y=45)

lbl13 = Label()
lbl13.config(text="#ff7f50",bg="gray")
lbl13.place(x=270,y=70)

lbl14 = Label()
lbl14.config(text="#00ffff",bg="gray")
lbl14.place(x=270,y=95)

lbl15 = Label()
lbl15.config(text="#8b8878",bg="gray")
lbl15.place(x=270,y=120)

lbl16 = Label()
lbl16.config(text="#006400",bg="gray")
lbl16.place(x=270,y=145)

lbl17 = Label()
lbl17.config(text="#bdb76b",bg="gray")
lbl17.place(x=270,y=170)

lbl18 = Label()
lbl18.config(text="#ff8c00",bg="gray")
lbl18.place(x=270,y=195)

lbl19 = Label()
lbl19.config(text="#9932cc",bg="gray")
lbl19.place(x=270,y=220)

lbl20 = Label()
lbl20.config(text="#8fbc8",bg="gray")
lbl20.place(x=270,y=245)












window.mainloop()