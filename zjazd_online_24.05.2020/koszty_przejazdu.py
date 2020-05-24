import tkinter

from tkinter import messagebox

def koszty_przejazdu():
    try:
        dystans = int(dystans_entry.get())
        spalanie = int(spalanie_entry.get())
        cena_paliwa = int(cena_paliwa_entry.get())
        suma = dystans * spalanie * cena_paliwa / 100
        koszt.configure(text=suma)
    except ValueError:
        messagebox.showerror("Błędne dane!!", "Popraw dane!")

root = tkinter.Tk()
dystans_label = tkinter.Label(master=root,text="Dystans")
dystans_label.pack()
dystans_entry = tkinter.Entry(master=root)
dystans_entry.pack()
spalanie_label = tkinter.Label(master=root,text="Spalanie")
spalanie_label.pack()
spalanie_entry = tkinter.Entry(master=root)
spalanie_entry.pack()
cena_paliwa_label = tkinter.Label(master=root,text="Cena_paliwa")
cena_paliwa_label.pack()
cena_paliwa_entry = tkinter.Entry(master=root)
cena_paliwa_entry.pack()

koszt_label = tkinter.Label(master=root, text="Wynik:")
koszt = tkinter.Label(master=root, text="")
koszt_label.pack()
koszt.pack()
submit = tkinter.Button(master=root, text="Policz", command=koszty_przejazdu)
submit.pack()

root.mainloop()

