import tkinter as  tk

root = tk.Tk()
root.title("Temperature Converter")
root.iconbitmap("termometro.ico")

numberInput= tk.StringVar()
var= tk.StringVar()

input_label= tk.Label(root, text="Enter Temperature")
input_entry= tk.Entry(root, textvariable=numberInput)

input_label.grid(row=0)
input_entry.grid(row=0, column=1)

dropdownList=["Celsius ", "Fahrenheit", "Kelvin "]
dropdown= tk.OptionMenu(root, var, *dropdownList)
var.set(dropdownList[0])
dropdown.grid(row=0, column=2)
root.mainloop()