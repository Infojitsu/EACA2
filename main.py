import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from math import *
import random
from datetime import datetime


root = tk.Tk()
root.title("Proiectul 2")
root.geometry("1200x900")  # Am redus dimensiunea pentru a încăpea cele două grafice pătrate

tabControl = ttk.Notebook(root)
tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)

tabControl.add(tab1, text='Pagina principala')
tabControl.add(tab2, text='Transformari uzuale')


tabControl.pack(expand=1, fill="both")


# create second figure and subplot
fig2, ax2 = plt.subplots()
fig2.set_size_inches(5, 5)  # set size to 4x4 inches pentru a face un pătrat


# set axis limits to include origin and make it visible
ax2.set_xlim(-10, 10)
ax2.set_ylim(-10, 10)

# add reference lines for the origin
ax2.axhline(0, color='black', linewidth=0.5)
ax2.axvline(0, color='black', linewidth=0.5)

# create a canvas to display the second graph
canvas2 = FigureCanvasTkAgg(fig2, master=tab1)
canvas2.draw()
canvas2.get_tk_widget().place(x=230, y=0)



# create first figure and subplot
fig1, ax1 = plt.subplots()
fig1.set_size_inches(5, 5)  # set size to 4x4 inches pentru a face un pătrat


# set axis limits to include origin and make it visible
ax1.set_xlim(-10, 10)
ax1.set_ylim(-10, 10)

# add reference lines for the origin
ax1.axhline(0, color='black', linewidth=0.5)
ax1.axvline(0, color='black', linewidth=0.5)

# create a canvas to display the first graph
canvas1 = FigureCanvasTkAgg(fig1, master=tab1)
canvas1.draw()
canvas1.get_tk_widget().place(x=730, y=0)




# 5 Conversie coordonate polare/trigonometrice în coordonate carteziene
def Trig2Cart(modul, argument):
    x = modul * cos(argument)
    y = modul * sin(argument)
    z = x + 1j * y
    return z

def Cart2Trig(z):
    x = z.real
    y = z.imag
    modul = sqrt(x ** 2 + y ** 2)
    argument = atan2(y, x)
    return (modul, argument)

ListaZ = []

def DeseneazaLista(ListaZ, culoare='blue', marime=10):
    ListaX = [z.real for z in ListaZ]
    ListaY = [z.imag for z in ListaZ]
    ax2.scatter(ListaX, ListaY, color=culoare, s=marime)
    ax2.set_xlim(-10, 10)  # Re-setam limitele axelor pentru a include originea
    ax2.set_ylim(-10, 10)
    ax2.axhline(0, color='black', linewidth=0.5)
    ax2.axvline(0, color='black', linewidth=0.5)
    canvas2.draw()
    return ListaZ

def DeseneazaLista2(ListaZ, culoare='blue', marime=10):
    ListaX = [z.real for z in ListaZ]
    ListaY = [z.imag for z in ListaZ]
    ax1.scatter(ListaX, ListaY, color=culoare, s=marime)
    ax1.set_xlim(-10, 10)  # Re-setam limitele axelor pentru a include originea
    ax1.set_ylim(-10, 10)
    ax1.axhline(0, color='black', linewidth=0.5)
    ax1.axvline(0, color='black', linewidth=0.5)
    canvas1.draw()
    return

def DeseneazaSegment1(z1, z2, NumarPuncte=100):
    ax2.clear()
    ax2.axhline(0, color='black', linewidth=0.5)
    ax2.axvline(0, color='black', linewidth=0.5)
    ListaZ = []
    for k in range(NumarPuncte):
        t = k / NumarPuncte
        z = (1 - t) * z1 + t * z2
        ListaZ.append(z)
    DeseneazaLista(ListaZ)
    return ListaZ


#=====================Segment==========================
tk.Label(tab1, text="z1 :").place(x=5, y=40)
tk.Label(tab1, text="z2 :").place(x=5, y=70)
segment_z1_entry = tk.Entry(tab1)
segment_z1_entry.place(x=30, y=40, width=70)
segment_z2_entry = tk.Entry(tab1)
segment_z2_entry.place(x=30, y=70, width=70)

# Desenam un segment cu capete date
def DeseneazaSegment(NumarPuncte=100):
    ax2.clear()
    ax2.axhline(0, color='black', linewidth=0.5)
    ax2.axvline(0, color='black', linewidth=0.5)
    ListaZ = []
    z1 = complex(segment_z1_entry.get())
    z2 = complex(segment_z2_entry.get())
    for k in range(NumarPuncte):
        t = k / NumarPuncte
        z = (1 - t) * z1 + t * z2
        ListaZ.append(z)
    DeseneazaLista(ListaZ)
    return ListaZ

def asoc_segm():
    global lst
    lst = DeseneazaSegment(NumarPuncte=1000)
    print(lst)

button1 = tk.Button(master=tab1, text="Deseneaza segment [z1,z2]", command=lambda: asoc_segm())
button1.place(x=10, y=10)
#======================================================================

#============================Cerc=========================================

tk.Label(tab1, text="z0 :").place(x=5, y=130)
tk.Label(tab1, text="r :").place(x=5, y=160)

centru_cerc_entry = tk.Entry(tab1)
centru_cerc_entry.place(x=30, y=130)
raza_cerc_entry = tk.Entry(tab1)
raza_cerc_entry.place(x=30, y=160)
lst = []

# Desenam un cerc
def DeseneazaCerc(NumarPuncte=1000):
    ax2.clear()
    ListaZ = []
    z0 = complex(centru_cerc_entry.get())
    r = float(raza_cerc_entry.get())
    for k in range(NumarPuncte):
        theta = 2 * pi * k / NumarPuncte
        z = z0 + Trig2Cart(r, theta)
        ListaZ.append(z)
    DeseneazaLista(ListaZ)
    return ListaZ

def asoc_cerc():
    global lst
    lst = DeseneazaCerc(NumarPuncte=1000)
    print(lst)

button2 = tk.Button(master=tab1, text="Deseneaza Cerc C(z0,r)", command=lambda: asoc_cerc())
button2.place(x=10, y=100)

#==================================================================

#=============================Patrat=====================================

tk.Label(tab1, text="z1 :").place(x=5, y=220)
tk.Label(tab1, text="z2 :").place(x=5, y=250)
tk.Label(tab1, text="z3 :").place(x=5, y=280)
tk.Label(tab1, text="z4 :").place(x=5, y=310)

patrat_z1_entry = tk.Entry(tab1)
patrat_z1_entry.place(x=30, y=220)
patrat_z2_entry = tk.Entry(tab1)
patrat_z2_entry.place(x=30, y=250)
patrat_z3_entry = tk.Entry(tab1)
patrat_z3_entry.place(x=30, y=280)
patrat_z4_entry = tk.Entry(tab1)
patrat_z4_entry.place(x=30, y=310)

def DeseneazaPatrat():
    ListaZz = []
    ax2.clear()
    z1 = complex(patrat_z1_entry.get())
    z2 = complex(patrat_z2_entry.get())
    z3 = complex(patrat_z3_entry.get())
    z4 = complex(patrat_z4_entry.get())
    patrat = DeseneazaSegment1(z1, z2) + DeseneazaSegment1(z2, z3) + DeseneazaSegment1(z3, z4) + DeseneazaSegment1(z4, z1)
    #patrat = DeseneazaSegment(1 + 1j, 2 + 1j) + DeseneazaSegment(2 + 1j, 2 + 2j) + DeseneazaSegment(2 + 2j,1 + 2j) + DeseneazaSegment(1 + 2j, 1 + 1j)
    ListaZz = DeseneazaLista(patrat)
    return ListaZz
    """

   
    
    ListaZz.append(DeseneazaSegment1(z1, z2))
    ListaZz.append(DeseneazaSegment1(z2, z3))
    ListaZz.append(DeseneazaSegment1(z3, z4))
    ListaZz.append(DeseneazaSegment1(z4, z1))
    return ListaZz"""

def asoc_patrat():
    global lst
    lst = DeseneazaPatrat()
    print(lst)

button3 = tk.Button(master=tab1, text="Deseneaza Patrulater", command=lambda: asoc_patrat())
button3.place(x=10, y=190)

#===================================================================

#========================Hexagon=======================================

tk.Label(tab1, text="z1 :").place(x=5, y=370)
tk.Label(tab1, text="z2 :").place(x=5, y=400)
tk.Label(tab1, text="z3 :").place(x=5, y=430)
tk.Label(tab1, text="z4 :").place(x=5, y=460)
tk.Label(tab1, text="z5 :").place(x=5, y=490)
tk.Label(tab1, text="z6 :").place(x=5, y=520)
hexagon_z1_entry = tk.Entry(tab1)
hexagon_z1_entry.place(x=30, y=370)
hexagon_z2_entry = tk.Entry(tab1)
hexagon_z2_entry.place(x=30, y=400)
hexagon_z3_entry = tk.Entry(tab1)
hexagon_z3_entry.place(x=30, y=430)
hexagon_z4_entry = tk.Entry(tab1)
hexagon_z4_entry.place(x=30, y=460)
hexagon_z5_entry = tk.Entry(tab1)
hexagon_z5_entry.place(x=30, y=490)
hexagon_z6_entry = tk.Entry(tab1)
hexagon_z6_entry.place(x=30, y=520)

def DeseneazaHexagon():
    ax2.clear()
    z1 = complex(hexagon_z1_entry.get())
    z2 = complex(hexagon_z2_entry.get())
    z3 = complex(hexagon_z3_entry.get())
    z4 = complex(hexagon_z4_entry.get())
    z5 = complex(hexagon_z5_entry.get())
    z6 = complex(hexagon_z6_entry.get())
    hexagon = DeseneazaSegment1(z1, z2) + DeseneazaSegment1(z2, z3) + DeseneazaSegment1(z3, z4) + DeseneazaSegment1(z4, z5) + DeseneazaSegment1(z5, z6) + DeseneazaSegment1(z6, z1)
    ListaZ = DeseneazaLista(hexagon)
    return ListaZ

def asoc_hexa():
    global lst
    lst = DeseneazaHexagon()
    print(lst)

button4 = tk.Button(master=tab1, text="Deseneaza Hexagon", command=lambda: asoc_hexa())
button4.place(x=10, y=340)

#=================================================================================

#===================================Disc===========================================

tk.Label(tab1, text="z0 :").place(x=5, y=580)
tk.Label(tab1, text="r :").place(x=5, y=610)

centru_disc_entry = tk.Entry(tab1)
centru_disc_entry.place(x=30, y=580)
raza_disc_entry = tk.Entry(tab1)
raza_disc_entry.place(x=30, y=610)

def DeseneazaDisc(NumarPuncte=1000):
    ax2.clear()
    ListaZ = []
    z0 = complex(centru_disc_entry.get())
    r = float(raza_disc_entry.get())
    i = np.linspace(0, r, 10000)
    for k in range(NumarPuncte):
        theta = 2 * pi * k / NumarPuncte
        z = z0 + Trig2Cart(i, theta)
        ListaZ.append(z)
    DeseneazaLista(ListaZ)
    return ListaZ

def asoc_disc():
    global lst
    lst = DeseneazaDisc(NumarPuncte=1000)
    print(lst)

button5 = tk.Button(master=tab1, text="Deseneaza Disc", command=lambda: asoc_disc())
button5.place(x=10, y=550)

#=================================================================

#====================Transformare=======================================

transformare_entry = tk.Entry(tab1)
transformare_entry.place(x=90, y=800)
n = tk.StringVar()
functii = ttk.Combobox(root, width = 27, textvariable = n)


def Transforma(lista, comanda):
    print(lista)
    ax1.clear()
    ax1.set_xlim(-10, 10)  # Re-setam limitele axelor pentru a include originea
    ax1.set_ylim(-10, 10)
    global lst
    lista_noua = []
    for z in lista:
        exec(f"lista_noua.append({comanda})")
    DeseneazaLista2(lista_noua)
    lst = []
    return


def actualizare_lista():
    with open("salvate.txt", "r") as f:
        optiuni = [(line.strip(),) for line in f.readlines()]
        return tuple(optiuni)

def salveaza():
    if (transformare_entry.get(),) not in functii["values"]:
        if transformare_entry.get() != "":
            with open("salvate.txt", "a") as f:
                f.write(transformare_entry.get() + "\n")
            functii['values'] = actualizare_lista()

def incarcare():
    transformare_entry.delete(0, tk.END)
    transformare_entry.insert(0, functii.get())

button6 = tk.Button(master=tab1, text="Transforma", command=lambda: Transforma(lst, transformare_entry.get()))
button6.place(x=10, y=800)

button7 = tk.Button(master=tab1, text="Salvare", command=lambda: salveaza())
button7.place(x=240, y=800)

button8 = tk.Button(master=tab1, text="Incarcare", command=lambda: incarcare())
button8.place(x=450, y=800)

button9 = tk.Button(master=tab1, text="Salvare imagine", command=lambda: plt.savefig(f'grafic_{datetime.now().strftime('%H_%M_%S')}.png'))
button9.place(x=950, y=500)




functii['values'] = actualizare_lista()

functii.place(x=400, y=800)
#====================================================================================


#============================Tab2===================================

tk.Label(tab2, text = "Transformari uzuale :").place(x=600, y=30)

tk.Label(tab2,text="- Translatia : z -> z+b").place(x=600, y=70)
tk.Label(tab2,text="- Omotetia : z -> z*a").place(x=600, y=100)
tk.Label(tab2,text="- Rotatia : z -> z*Trig2Cart(1,t)").place(x=600, y=130)
tk.Label(tab2,text="- Simetrie : z -> z.conjugate()").place(x=600, y=160)
tk.Label(tab2,text="- Inversiune : z -> 1/z").place(x=600, y=190)


#=====================================================================


#=================================Extra=====================================




def iesire():
    # Inițializare fereastră principală
    window = tk.Tk()
    window.title("Inchidere aplicatie")
    window.geometry("400x200")  # Dimensiune mai mare a ferestrei

    # Adăugare etichete și butoane
    label = tk.Label(window, text="Primim nota buna la proiect ? ")
    label.pack(pady=20)

    yes_btn = tk.Button(window, text="Da", command=quit)
    yes_btn.pack(side=tk.LEFT, padx=50, pady=20)

    no_btn = tk.Button(window, text="Nu")
    no_btn.pack(side=tk.RIGHT, padx=50, pady=20)

    def move_button(event):
        x = random.randint(0, window.winfo_width() - no_btn.winfo_width())
        y = random.randint(0, window.winfo_height() - no_btn.winfo_height())
        no_btn.place(x=x, y=y)

    # Asocierea evenimentului de mișcare a cursorului cu butonul 'Nu'
    no_btn.bind("<Enter>", move_button)



    # Rulare buclă principală Tkinter
    window.mainloop()



root.wm_protocol("WM_DELETE_WINDOW", iesire)


root.mainloop()
