import random
import tkinter as tk
from tkinter import *
from tkinter import messagebox


def oyna(*args):
    global sayac
    while sayac < 14:
        breaker_listesi = list(data.get())
        if breaker_listesi == renkler_listesi:
            return messagebox.showinfo("Mastermind", "Doğru bildiniz!")
        if set(breaker_listesi).issubset(set(renkler)) and len(breaker_listesi) == 4:
            renkler_dict = {k: v for k, v in enumerate(renkler_listesi, start=1)}
            breaker_dict = {k: v for k, v in enumerate(breaker_listesi, start=1)}
            black, white = 0, 0
            flag1 = 1
            flag2 = 1
            for key, value in breaker_dict.items():
                if value == 'b':
                    f = 'blue'
                    canvas.create_oval(20 + 60 * (flag2 - 1), 10 + (50 * sayac), 50 + 60 * (flag2 - 1),
                                       40 + (50 * sayac), width=1, fill=f)
                    flag2 += 1
                elif value == 'y':
                    f = 'yellow'
                    canvas.create_oval(20 + 60 * (flag2 - 1), 10 + (50 * sayac), 50 + 60 * (flag2 - 1),
                                       40 + (50 * sayac), width=1, fill=f)
                    flag2 += 1
                elif value == 'r':
                    f = 'red'
                    canvas.create_oval(20 + 60 * (flag2 - 1), 10 + (50 * sayac), 50 + 60 * (flag2 - 1),
                                       40 + (50 * sayac), width=1, fill=f)
                    flag2 += 1
                elif value == 'c':
                    f = 'cyan'
                    canvas.create_oval(20 + 60 * (flag2 - 1), 10 + (50 * sayac), 50 + 60 * (flag2 - 1),
                                       40 + (50 * sayac), width=1, fill=f)
                    flag2 += 1
                elif value == 'g':
                    f = 'green'
                    canvas.create_oval(20 + 60 * (flag2 - 1), 10 + (50 * sayac), 50 + 60 * (flag2 - 1),
                                       40 + (50 * sayac), width=1, fill=f)
                    flag2 += 1
                elif value == 'm':
                    f = 'magenta'
                    canvas.create_oval(20 + 60 * (flag2 - 1), 10 + (50 * sayac), 50 + 60 * (flag2 - 1),
                                       40 + (50 * sayac), width=1, fill=f)
                    flag2 += 1

                if renkler_dict[key] == value:
                    black += 1
                    if flag1 == 1:
                        canvas.create_oval(260, 10 + (50 * sayac), 270, 20 + (50 * sayac), width=1, fill='black')
                        flag1 += 1
                    elif flag1 == 2:
                        canvas.create_oval(280, 10 + (50 * sayac), 290, 20 + (50 * sayac), width=1, fill='black')
                        flag1 += 1
                    elif flag1 == 3:
                        canvas.create_oval(260, 25 + (50 * sayac), 270, 35 + (50 * sayac), width=1, fill='black')
                        flag1 += 1
                    elif flag1 == 4:
                        canvas.create_oval(280, 25 + (50 * sayac), 290, 35 + (50 * sayac), width=1, fill='black')
                elif value in renkler_dict.values():
                    white += 1
                    if flag1 == 1:
                        canvas.create_oval(260, 10 + (50 * sayac), 270, 20 + (50 * sayac), width=1, fill='white')
                        flag1 += 1
                    elif flag1 == 2:
                        canvas.create_oval(280, 10 + (50 * sayac), 290, 20 + (50 * sayac), width=1, fill='white')
                        flag1 += 1
                    elif flag1 == 3:
                        canvas.create_oval(260, 25 + (50 * sayac), 270, 35 + (50 * sayac), width=1, fill='white')
                        flag1 += 1
                    elif flag1 == 4:
                        canvas.create_oval(280, 25 + (50 * sayac), 290, 35 + (50 * sayac), width=1, fill='white')

            sayac += 1
            print("black: " + str(black), "white: " + str(white))
            return "black: " + str(black), "white: " + str(white), sayac
        elif not len(breaker_listesi) == 4:
            return messagebox.showwarning("Mastermind", "Yanlış sayıda renk girdiniz. 4 karakter girmelisiniz. "
                                                        "Tekrar renk giriniz.")
        else:
            return messagebox.showwarning("Mastermind", "Listede olmayan bir renk kombinasyonu girdiniz. "
                                                        "Tekrar renk giriniz.")
    return messagebox.showinfo("Mastermind", "Bilemediniz ve hakkınız bitti!")


if __name__ == '__main__':
    renkler = ["b", "y", "r", "c", "g", "m"]
    renkler_listesi = []
    while True:
        i = (random.choice(renkler))
        if renkler_listesi.count(i) == 2:
            pass
        else:
            renkler_listesi.append(i)
        if len(renkler_listesi) == 4:
            break
        else:
            continue
    sayac = 1

    win = tk.Tk()

    # Define the geometry of window
    win.geometry("350x800")

    # Create a canvas object
    canvas = tk.Canvas(win, width=350, height=800, bg="SandyBrown")

    canvas.create_oval(20, 10, 50, 40, width=1, fill='black')
    canvas.create_oval(80, 10, 110, 40, width=1, fill='black')
    canvas.create_oval(140, 10, 170, 40, width=1, fill='black')
    canvas.create_oval(200, 10, 230, 40, width=1, fill='black')
    canvas.create_line(10, 50, 340, 50, width=2, fill='gray')

    for i in range(1, 14):
        canvas.create_oval(20, 10+(50*i), 50, 40+(50*i), width=1, fill='gray')
        canvas.create_oval(80, 10+(50*i), 110, 40+(50*i), width=1, fill='gray')
        canvas.create_oval(140, 10+(50*i), 170, 40+(50*i), width=1, fill='gray')
        canvas.create_oval(200, 10+(50*i), 230, 40+(50*i), width=1, fill='gray')
        canvas.create_oval(260, 10+(50*i), 270, 20+(50*i), width=1, fill='gray')
        canvas.create_oval(280, 10+(50*i), 290, 20+(50*i), width=1, fill='gray')
        canvas.create_oval(260, 25+(50*i), 270, 35+(50*i), width=1, fill='gray')
        canvas.create_oval(280, 25+(50*i), 290, 35+(50*i), width=1, fill='gray')
        canvas.create_line(10, 50+(50*i), 340, 50+(50*i), width=2, fill='gray')

    L1 = tk.Label(win, text="Tahmin giriniz")
    L1.pack(side=BOTTOM)
    data = tk.Entry(win, bd=5, width=5)
    data.bind("<Return>", oyna)
    data.pack(side=BOTTOM)

    canvas.pack()
    win.mainloop()
