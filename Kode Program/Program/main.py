##LIBRARY
from apartemen import Apartemen
from rumah import Rumah
from indekos import Indekos
from tkinter import *
import os

#CLASS
hunians = []
hunians.append(Apartemen("Nelly Joy", 3, 3))
hunians.append(Rumah("Sekar MK", 5, 2))
hunians.append(Indekos("Bp. Romi", "Cahya"))
hunians.append(Rumah("Satria", 1, 4))
hunians.append(Apartemen("Cantika", 1, 4))

root = Tk()
root.title("Latihan Praktikum 9 DPBO")

## Detail 
def details(index):
    top = Toplevel()
    top.title("Detail " + hunians[index].get_jenis())
    
    current_dir = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(current_dir, "../images/rumah.png")
    
    logo_image = PhotoImage(file=image_path).subsample(3)
    top.image = logo_image

    frame = LabelFrame(top, padx=10, pady=10, width=400, height=300)
    frame.pack(padx=10, pady=10)
    
    frame_label = Label(frame, image=logo_image)
    frame_label.pack()

    d_frame = LabelFrame(top, text="Detail Residen", padx=10, pady=10)
    d_frame.pack(padx=10, pady=10)

    d_summary = Label(d_frame, text="Summary\n" + hunians[index].get_detail() + hunians[index].get_summary() + "\n" + hunians[index].get_dokumen(), anchor="w", justify=LEFT)
    d_summary.pack()

    btn = LabelFrame(top, padx=0, pady=0)
    btn.pack(padx=0, pady=0)
    b_close = Button(top, text="Close", command=top.destroy)
    b_close.pack()

## Home Page
def home():
    top = Toplevel()
    top.title("Homepage Daftar Residen")

    frame = LabelFrame(top, text="Data Seluruh Residen", padx=10, pady=10)
    frame.pack(padx=10, pady=10)

    for index, h in enumerate(hunians):
        idx = Label(frame, text=str(index+1), width=5, borderwidth=1, relief="solid")
        idx.grid(row=index, column=0)

        type_label = Label(frame, text=h.get_jenis(), width=15, borderwidth=1, relief="solid")
        type_label.grid(row=index, column=1)

        if h.get_jenis() != "Indekos": 
            name_label = Label(frame, text=" " + h.get_nama_pemilik(), width=40, borderwidth=1, relief="solid", anchor="w")
            name_label.grid(row=index, column=2)
        else:
            name_label = Label(frame, text=" " + h.get_nama_penghuni(), width=40, borderwidth=1, relief="solid", anchor="w")
            name_label.grid(row=index, column=2)

        b_detail = Button(frame, text="Details ", command=lambda index=index: details(index))
        b_detail.grid(row=index, column=3)

    btn = LabelFrame(top, padx=0, pady=0)
    btn.pack(padx=0, pady=0)
    b_close = Button(top, text="Exit", command=top.destroy)
    b_close.pack()

## Landing Page

current_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(current_dir, "../images/landing_page.png")
logo_image = PhotoImage(file=image_path).zoom(2)

frame_label = Label(root, text="Welcome Fellas!", font=("Times new roman", 12, "bold"))
frame_label.pack()

frame_label = Label(root, image=logo_image)
frame_label.pack()

opts = LabelFrame(root, padx=0, pady=0)
opts.pack(padx=0, pady=0)

b_daftar = Button(opts, text="Get Here", command=home)
b_daftar.grid(row=0, column=0)

root.mainloop()