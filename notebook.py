from tkinter import *
from tkinter import ttk, messagebox

root = Tk()
root.title("Hello")
root.geometry("250x400")



main_menu = Menu(root)
main_menu.add_command(label="Файл")
main_menu.add_command(label="Изменить")
main_menu.add_command(label="Формат")
main_menu.add_command(label="Вид")
main_menu.add_command(label="Справка")
root.config(menu=main_menu)

text_editor = Text()
text_editor.grid(column=0, columnspan=2, row=0)
scrollbar = ttk.Scrollbar(orient=VERTICAL)
scrollbar.grid(row=0, column=1, sticky="ns")

root.mainloop()
