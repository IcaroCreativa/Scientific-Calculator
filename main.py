from tkinter import *
from calculator import *
import math

formule = "" 

def click(num): 

    global formule 
    formule = formule + str(num) 
    equation.set(formule) 

def equalclick(): 
    try: 
        global formule 
        result = str(calculator(formule)) 
        equation.set(result) 
        formule = result

    except: 
        equation.set(" error ") 
        formule = "" 

def effacer(): 
    global formule 
    formule = "" 
    equation.set("")

def backspace():
    global formule
    formule=formule[:-1]
    equation.set(formule) 
   

if __name__ == "__main__": 
    master = Tk() 
    master.title("Calculatrice") 
    master.geometry("530x315")
    master.resizable(width=False, height=False)
    equation = StringVar() 
    formule_field = Entry(master, textvariable=equation) 
    formule_field.grid(columnspan=4,  pady= 30 , padx = 20 , ipadx = 100 , ipady = 10)
    btn_1 = Button(master, text=' 1 ', command=lambda: click(1), height=2, width=10) 
    btn_1.grid(row=2, column=0) 

    btn_2 = Button(master, text=' 2 ', command=lambda: click(2), height=2, width=10) 
    btn_2.grid(row=2, column=1) 

    btn_3 = Button(master, text=' 3 ', command=lambda: click(3), height=2, width=10) 
    btn_3.grid(row=2, column=2) 

    btn_4 = Button(master, text=' 4 ', command=lambda: click(4), height=2, width=10) 
    btn_4.grid(row=3, column=0) 

    btn_5 = Button(master, text=' 5 ', command=lambda: click(5), height=2, width=10) 
    btn_5.grid(row=3, column=1) 

    btn_6 = Button(master, text=' 6 ', command=lambda: click(6), height=2, width=10) 
    btn_6.grid(row=3, column=2) 

    btn_7 = Button(master, text=' 7 ', command=lambda: click(7), height=2, width=10) 
    btn_7.grid(row=4, column=0) 

    btn_8 = Button(master, text=' 8 ', command=lambda: click(8), height=2, width=10) 
    btn_8.grid(row=4, column=1) 

    btn_9 = Button(master, text=' 9 ', command=lambda: click(9), height=2, width=10) 
    btn_9.grid(row=4, column=2) 

    btn_0 = Button(master, text=' 0 ', command=lambda: click(0), height=2, width=10) 
    btn_0.grid(row=5, column=0) 

    plus = Button(master, text=' + ', command=lambda: click("+"), height=2, width=10) 
    plus.grid(row=2, column=3) 

    minus = Button(master, text=' - ', command=lambda: click("-"), height=2, width=10) 
    minus.grid(row=3, column=3) 

    multiply = Button(master, text=' * ', command=lambda: click("*"), height=2, width=10) 
    multiply.grid(row=4, column=3) 

    divide = Button(master, text=' / ', command=lambda: click("/"), height=2, width=10) 
    divide.grid(row=5, column=3) 

    equal = Button(master, text=' = ', command=equalclick, height=2, width=10) 
    equal.grid(row=5, column=2) 

    effacer = Button(master, text='effacer', command=effacer, height=2, width=10) 
    effacer.grid(row=6, column='0') 

    Decimal= Button(master, text='.', command=lambda: click('.'), height=2, width=10) 
    Decimal.grid(row=5, column=1) 
    
    percent= Button(master, text='%', command=lambda: click('%'), height=2, width=10) 
    percent.grid(row=6, column=1) 
    
    inverse= Button(master, text='1/X',  height=2, width=10) 
    inverse.grid(row=6, column=2) 
    
    memo= Button(master, text='M',  height=2, width=10) 
    memo.grid(row=6, column=3)  

    parenteses_open = Button(master, text=' ( ', command=lambda: click("("), height=2, width=10)
    parenteses_open.grid(row=2, column=4)

    parenteses_close = Button(master, text=' ) ', command=lambda: click(")"), height=2, width=10)
    parenteses_close.grid(row=3, column=4)

    backspace_btn= Button(master, text=' <- ', command=lambda: backspace(), height=2, width=10)
    backspace_btn.grid(row=4, column=4)
      
    pi_btn= Button(master, text='\u03C0', command=lambda: click(str(math.pi)), height=2, width=10)
    pi_btn.grid(row=5, column=4) 
    
    square_btn= Button(master, text='\u221A', command=lambda: click('0#'), height=2, width=10)
    square_btn.grid(row=6, column=4)

    cos_btn= Button(master, text='cos', command=lambda: click('0C'), height=2, width=10)
    cos_btn.grid(row=2, column=5)

    sin_btn= Button(master, text='sin', command=lambda: click('0S'), height=2, width=10)
    sin_btn.grid(row=3, column=5)

    tan_btn= Button(master, text='tan', command=lambda: click('0T'), height=2, width=10)
    tan_btn.grid(row=4, column=5)   
    
    master.mainloop()
