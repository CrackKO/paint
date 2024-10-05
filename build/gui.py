
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, filedialog, messagebox
from customtkinter import *

OUTPUT_PATH = Path(__file__).parent

# ASSETS_PATH = OUTPUT_PATH / Path(r"F:\paint\build\assets\frame0")
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\ilyxa_paint\paint\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)
import webbrowser
def gitlink():
    webbrowser.open("https://github.com/CrackKO/paint")

window = CTk()
window.geometry("1920x1080")
bg1 = "#171717"
yq = False
window.configure(bg = bg1)


canvas = Canvas(
    window,
    bg = bg1,
    height = 1080,
    width = 1920,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)
canvas.place(x = 0, y = 0)


def open():
    file_path = filedialog.askopenfilename(
        title="Откройте файл .png",
        filetypes=[("PNG", "*.png")] #Указываем тип файла который выбираем
    )
    if file_path:
        label = CTkLabel(master=window, text=f"Готово", font=("Lexend",20), text_color="#00FF00")
        label.place(relx = 0.5, rely = 0.4, anchor = "center")
    else:
        messagebox.showwarning("Нет файла", "Файл не был выбран") #В случае если ты не выбрал файл то будет эта хуйня

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    activebackground="#171717",
    command=gitlink,
    relief="flat",
)
button_1.place(
    x=865.0,
    y=600.0,
    width=189.0,
    height=53.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))

button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    activebackground="#171717",
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=995.0,
    y=426.0,
    width=160.0,
    height=49.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    activebackground="#171717",
    highlightthickness=0,
    command=open,
    relief="flat"
)
button_3.place(
    x=764.0,
    y=426.0,
    width=160.0,
    height=49.0
)

def colorthem2():
    if checkbox.get():
        bg1 = "#FFFFFF"
        yq = True
        open_button_dark=relative_to_assets("Button1.png")
        create_button_dark=relative_to_assets("Button2.png")
        git_button_dark=relative_to_assets("Button3.png")
    else:
        bg1 = "#171717"
        yq = False
        open_button_dark=relative_to_assets("button_3.png")
        create_button_dark=relative_to_assets("button_2.png")
        git_button_dark=relative_to_assets("button_1.png")
    
    canvas.config(bg=bg1)
    button_image_3.config(file=open_button_dark)
    button_image_2.config(file=create_button_dark)
    button_image_1.config(file=git_button_dark)

    if yq == False:
        checkbox.configure(text_color = "#FFFFFF", bg_color = bg1)
    else:
        checkbox.configure(text_color = "#171717", bg_color = bg1)

checkbox = CTkCheckBox(
     master=window,
     text="Switch Theme",
     text_color = bg1,
     bg_color = bg1,
     fg_color="#C850C0",
     checkbox_height=20,
     checkbox_width=20,
     corner_radius=36,
     command=colorthem2)


checkbox.place(
     relx = 0.5, 
     rely = 0.50, 
     anchor = "center")

window.resizable(False, False)
window.mainloop()
print(False)
