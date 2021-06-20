from tkinter import *
from functools import partial

root = Tk()
root.title("Convertor de Temperatura")
root.iconbitmap("termometro.ico")

valor_temp="Celsius"

def store_temp(sel_temp):
    global valor_temp
    temVal=sel_temp

def call_result(rl1, rl2, inputn):
    tem= inputn.get()
    if temVal == "Celsius":
        f = float((float(tem) * 9/5) + 32)
        k = float((float(tem) + 273.15))
        rl1.config(text="%f Fahrenheit" % f)
        rl2.config(text="%f Kelvin" % k)
    if temVal == "Fahrenheit":
        c = float((float(tem)- 32) * 5/9)
        k = c + 273
        rl1.config(text="%f Celsius" % c)
        rl2.config(text="%f Kelvin" % k)
    if temVal == "Kelvin":
        c = float((float(tem)- 273.15))
        f = float((float(tem) - 273.15) * 1.8000 + 32.00)
        rl1.config(text="%f Celsius" % c)
        rl2.config(text="%f Fahrenheit" % f)
    return

numberInput= StringVar()
var= StringVar()


input_label= Label(root, text="Enter Temperature")
input_entry= Entry(root, textvariable=numberInput)


input_label.grid(row=0)
input_entry.grid(row=0, column=1)


rLabel_1= Label(root, text="Result1")
rLabel_1.grid(row=3, columnspan=4)
rLabel_2=Label(root, text="Result2")
rLabel_2.grid(row=4, columnspan=4)

call_result=partial(call_result, rLabel_1, rLabel_2, numberInput)
result_button= Button(root, text="Convert", command=call_result)
result_button.grid(row=1, columnspan=4)

dropdownList=["Celsius", "Fahrenheit", "Kelvin"]
dropdown= OptionMenu(root, var, *dropdownList, command=store_temp )
var.set(dropdownList[0])
dropdown.grid(row=0, column=2)
root.mainloop()