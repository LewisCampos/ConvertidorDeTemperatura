from tkinter import *
from functools import partial

raiz = Tk()
raiz.title("Convertidor de Temperatura")
raiz.iconbitmap("termometro.ico")

valor_temp="Celsius"

def temperaturas(temp_sel):
    global valor_temp
    valor_temp=temp_sel

def resultado(rEt1, rEt2, valor):
    tem= valor.get()
    while True:
        try:
            if valor_temp == "Celsius":
                f = float((float(tem) * 9/5) + 32)
                k = float((float(tem) + 273.15))
                rEt1.config(text="%f Fahrenheit" % f)
                rEt2.config(text="%f Kelvin" % k)
            elif valor_temp == "Fahrenheit":
                c = float((float(tem)- 32) * 5/9)
                k = c + 273
                rEt1.config(text="%f Celsius" % c)
                rEt2.config(text="%f Kelvin" % k)
            else:
                c = float((float(tem)- 273.15))
                f = float((float(tem) - 273.15) * 1.8000 + 32.00)
                rEt1.config(text="%f Celsius" % c)
                rEt2.config(text="%f Fahrenheit" % f)
            return
            break
        except:
            rEt1.config(text="ERROR, Valor no admitido..!!")
            rEt2.config(text="ERROR, Valor no admitido..!!")
            break

numero_ingresado= StringVar()
var= StringVar()


Etqt_1= Label(raiz, text="Ingrese Temperatura")
Etqt_entrada= Entry(raiz, textvariable=numero_ingresado)


Etqt_1.grid(row=0)
Etqt_entrada.grid(row=0, column=1)


rEtqt_1= Label(raiz, text="Result1")
rEtqt_1.grid(row=3, columnspan=4)
rEtqt_2=Label(raiz, text="Result2")
rEtqt_2.grid(row=4, columnspan=4)

resultado_final=partial(resultado, rEtqt_1, rEtqt_2, numero_ingresado)
boton_resultado= Button(raiz, text="Convertir", command=resultado_final)
boton_resultado.grid(row=1, columnspan=4)

lista_unidades=["Celsius", "Fahrenheit", "Kelvin"]
boton_menu= OptionMenu(raiz, var, *lista_unidades, command=temperaturas)
var.set(lista_unidades[0])
boton_menu.grid(row=0, column=2)
raiz.mainloop()