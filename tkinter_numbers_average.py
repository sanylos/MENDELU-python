import tkinter as tk
from tkinter import messagebox
okno = tk.Tk()
poz = '#55ff99'
okno.title('cs')
okno.configure(bg=poz)
okno.geometry('400x500')

pocetCisel = 0
soucet=0
def precti_cislo():
    global soucet
    global pocetCisel
    try:
        soucet+=int(vstup1.get())
        pocetCisel+=1
        vstup1.delete(0,tk.END)
        popisekSoucet.config(text="Součet čísel je {}".format(soucet))
    except:
        messagebox.showinfo('Pozor!!!','Asi jste nezadali číslo!')

def vypis_prumer():
    messagebox.showinfo('Průměr','Průměr: {}'.format(soucet/pocetCisel))

tlacitko_konec=tk.Button(okno,text='Zavřít',command=okno.destroy)
tlacitko_konec.pack(pady=10)

popisek1=tk.Label(okno,text='Zadej číslo',bg=poz, font=('Calibri',18))
popisek1.pack(pady=10)
vstup1=tk.Entry(okno)
vstup1.pack(pady=10)

tlacitko_konec=tk.Button(okno,text='Zpracuj číslo',command=precti_cislo,font=('Calibri',18))
tlacitko_konec.pack(pady=10)

popisekSoucet=tk.Label(okno,text='Součet čísel je: {}'.format(soucet),bg=poz, font=('Calibri',18))
popisekSoucet.pack(pady=10)

tlacitko_prumer=tk.Button(okno,text='Vypiš průměr',command=vypis_prumer,font=('Calibri',18))
tlacitko_prumer.pack(pady=10)

okno.mainloop()