import tkinter as  tk

root = tk.Tk()
root.title("Temperature Converter")
root.iconbitmap("termometro.ico")

numberInput= tk.StringVar()
var= tk.StringVar()

input_label= tk.Label(root, text="Enter Temperature")
input_entry= tk.Entry(root, textvariable=numberInput)
result_button= tk.Button(root, text="Convert")

input_label.grid(row=0)
input_entry.grid(row=0, column=1)
result_button.grid(row=2, columnspan=4)

rLabel_1= tk.Label(root, text="Result1")
rLabel_1.grid(row=3, columnspan=4)
rLabel_2= tk.Label(root, text="Result2")
rLabel_2.grid(row=4, columnspan=4)

dropdownList=["Celsius ", "Fahrenheit", "Kelvin "]
dropdown= tk.OptionMenu(root, var, *dropdownList)
var.set(dropdownList[0])
dropdown.grid(row=0, column=2)
root.mainloop()