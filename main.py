from tkinter import *
import time

root = Tk() #очистка всех перемен / выставить каждой перемене значение 0

root.title("черепашьи рисунки Кирилла")
root.geometry("300x300")
 
canvas = Canvas(bg="white", width=250, height=250)
canvas.pack(anchor=CENTER, expand=1) #до зтой строчки (включительно) подготовка к рисованию
c = 1.0


while True :
    c = 0.0+c+1
    a = c+c+c
    b = c-c-c
    canvas.create_line(a, 0, 0, b) #начало рисования
    print("ok")
    canvas.update()
    time.sleep(1)
    root.update()

