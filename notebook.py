from tkinter import *
from tkinter import filedialog
from tkinter import ttk

root = Tk()
root.title("Hello")
root.geometry("400x400")


def open_file():
    filepath = filedialog.askopenfilename()
    if filepath != "":
        with open(filepath, "r") as file:
            text = file.read()
            text_editor.delete("1.0", END)
            text_editor.insert("1.0", text)


def save_file():
    filepath = filedialog.asksaveasfilename()
    if filepath != "":
        text = text_editor.get("1.0", END)
        with open(filepath, "w") as file:
            file.write(text)


def new_file():
    filepath = filedialog.asksaveasfilename()
    if filepath != "":
        text = text_editor.get("1.0", END)
        with open(filepath, "w") as file:
            file.write(text)
    text_editor.delete('1.0', END)


copy_text = ''


def cut():
    global copy_text
    copy_text = text_editor.selection_get()
    text_editor.delete("sel.first", "sel.last")


def paste():
    global copy_text
    text_editor.insert(INSERT, copy_text)


def copy():
    global copy_text
    copy_text = text_editor.selection_get()


def undo():
    text_editor.edit_undo()


def redo():
    text_editor.edit_redo()


def clear():
    text_editor.delete('1.0', END)


main_menu = Menu(root)

file_menu = Menu()
file_menu.add_command(label='Новый файл', command=new_file)
file_menu.add_command(label='Открыть', command=open_file)
file_menu.add_command(label='Сохранить', command=save_file)
main_menu.add_cascade(label="Файл", menu=file_menu)

refactor_menu = Menu()
refactor_menu.add_command(label='Копировать', command=copy)
refactor_menu.add_command(label='Вставить', command=paste)
refactor_menu.add_command(label='Вырезать', command=cut)
refactor_menu.add_command(label='Очистить', command=clear)
main_menu.add_cascade(label="Изменить", menu=refactor_menu)

main_menu.add_cascade(label="Формат")
format_menu = Menu()

main_menu.add_cascade(label="Вид")
view_menu = Menu()

main_menu.add_cascade(label="Справка")
root.config(menu=main_menu)
frame = Frame()

text_editor = Text(wrap="none")
text_editor.grid(column=0, row=0, sticky=NSEW)

ys = ttk.Scrollbar(orient="vertical", command=text_editor.yview)
ys.grid(column=1, row=0, sticky=NS)

root.mainloop()
