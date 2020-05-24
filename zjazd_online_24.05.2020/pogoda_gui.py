import tkinter
from tkinter import messagebox
from pogoda import get_location_id,get_location_weather,report

def weather_Viewer():

    try:
        lokacja = lokacja_entry.get()
        l = get_location_id(lokacja)
        w = get_location_weather(l)
        wynik.configure(text=report(w,lokacja))

    except ValueError:
        messagebox.showerror("Błędne dane!!", "Popraw dane!")


root = tkinter.Tk()

pogoda_label = tkinter.Label(master=root, text="Podaj lokalizację: ")
pogoda_label.pack()

lokacja_entry = tkinter.Entry(master=root)
lokacja_entry.pack()


wynik = tkinter.Label(master=root, text="")
wynik.pack()

submit = tkinter.Button(master=root, text="Pokaż pogodę", command= weather_Viewer)
submit.pack()

root.mainloop()




