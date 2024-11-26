from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage, filedialog, messagebox, Label
from customtkinter import *
import webbrowser

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH_1 = OUTPUT_PATH / Path(r"F:\paint\build\assets\frame0")
ASSETS_PATH_2 = OUTPUT_PATH / Path(r"F:\paint\build2\assets\frame1")
# ASSETS_PATH_1 = OUTPUT_PATH / Path(r"D:\arigato\paint\build2\assets\frame0")
# ASSETS_PATH_2 = OUTPUT_PATH / Path(r"D:\arigato\paint\build2\assets\frame1")

def relative_to_assets_1(path: str) -> Path:
    return ASSETS_PATH_1 / Path(path)

def relative_to_assets_2(path: str) -> Path:
    return ASSETS_PATH_2 / Path(path)

def gitlink():
    webbrowser.open("https://github.com/CrackKO/paint")

def main_window():
    window = CTk()
    window.attributes("-fullscreen",True)
    window.geometry("1920x1080")
    bg1 = "#171717"
    window.configure(bg=bg1)

    canvas = Canvas(
        window,
        bg=bg1,
        height=1080,
        width=1920,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )
    canvas.place(x=0, y=0)

    def open_second_slide():
        window.destroy()  
        second_window()

    button_image_2 = PhotoImage(file=relative_to_assets_1("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        activebackground="#171717",
        command=open_second_slide,
        relief="flat"
    )
    button_2.place(x=995.0, y=426.0, width=160.0, height=49.0)

    button_image_3 = PhotoImage(file=relative_to_assets_1("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        activebackground="#171717",
        command=lambda: filedialog.askopenfilename(
            title="Откройте файл .png",
            filetypes=[("PNG", "*.png")]
        ),
        relief="flat"
    )
    button_3.place(x=764.0, y=426.0, width=160.0, height=49.0)

    button_image_1 = PhotoImage(file=relative_to_assets_1("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        activebackground="#171717",
        command=gitlink,
        relief="flat"
    )
    button_1.place(x=865.0, y=600.0, width=189.0, height=53.0)

    window.resizable(False, False)
    window.mainloop()

def second_window():

    def start_drawing(event):
        global last_x, last_y
        last_x, last_y = event.x, event.y

    def draw(event):
        global last_x, last_y
        canvas.create_line(
            last_x, last_y, event.x, event.y,
            fill="black",  # Цвет линии
            width=brush_size,  # Толщина линии
            capstyle="round"  # Закругленные линии
        )
        last_x, last_y = event.x, event.y

    window = Tk()
    window.state('normal')
    window.attributes("-fullscreen",True)
    window.geometry("1920x1080")
    window.configure(bg="#202020")

    canvas = Canvas(
        window,
        bg="#202020",
        height=1080,
        width=1920,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )
    canvas.pack(fill="both", expand=True)
    global last_x, last_y
    global brush_size
    brush_size = 5 
    def select_brush():
        """Активировать рисование кистью."""
        canvas.bind("<Button-1>", start_drawing)  # Нажатие кнопки мыши
        canvas.bind("<B1-Motion>", draw)
        
    bar = PhotoImage(file=relative_to_assets_2("da.png"))
    label = Label(window, background="#202020", image=bar)
    label.pack()
    label.place(x=225, y=999)

    brush_im = PhotoImage(file=relative_to_assets_2("1.png"))
    brush_btn = Button(
        image=brush_im,
        borderwidth=0,
        highlightthickness=0,
        bg="#D9D9D9",
        activebackground="#D9D9D9",
        relief="flat",
        command=select_brush
    )
    brush_btn.place(x=505.0, y=1005.0, width=50.0, height=50.0)

    pencil_im = PhotoImage(file=relative_to_assets_2("2.png"))
    pencil_btn = Button(
        image=pencil_im,
        borderwidth=0,
        highlightthickness=0,
        bg="#D9D9D9",
        activebackground="#D9D9D9",
        relief="flat"
    )
    pencil_btn.place(x=655.0, y=1005.0, width=50.0, height=50.0)

    eraser_im = PhotoImage(file=relative_to_assets_2("3.png"))
    eraser_btn = Button(
        image=eraser_im,
        borderwidth=0,
        highlightthickness=0,
        bg="#D9D9D9",
        activebackground="#D9D9D9",
        relief="flat"
    )
    eraser_btn.place(x=805.0, y=1005.0, width=50.0, height=50.0)

    ely_logo_im = PhotoImage(file=relative_to_assets_2("4.png"))
    ely_logo_btn = Button(
        image=ely_logo_im,
        borderwidth=0,
        highlightthickness=0,
        bg="#D9D9D9",
        activebackground="#D9D9D9",
        relief="flat"
    )
    ely_logo_btn.place(x=955.0, y=1005.0, width=50.0, height=50.0)
    

    tk_textbox = CTk.CTkTextbox(CTk, activate_scrollbars=False)
    tk_textbox.grid(row=0, column=0, sticky="nsew")
    ctk_textbox_scrollbar = CTk.CTkScrollbar(CTk, command=tk_textbox.yview)
    ctk_textbox_scrollbar.grid(row=0, column=1, sticky="ns")
    
    txt_im = PhotoImage(file=relative_to_assets_2("5.png"))
    txt_btn = Button(
        image=txt_im,
        borderwidth=0,
        highlightthickness=0,
        bg="#D9D9D9",
        activebackground="#D9D9D9",
        relief="flat"
    )
    txt_btn.place(x=1105.0, y=1005.0, width=50.0, height=50.0)

    shapes_im = PhotoImage(file=relative_to_assets_2("6.png"))
    shapes_btn = Button(
        image=shapes_im,
        borderwidth=0,
        highlightthickness=0,
        bg="#D9D9D9",
        activebackground="#D9D9D9",
        relief="flat"
    )
    shapes_btn.place(x=1255.0, y=1005.0, width=50.0, height=50.0)

    filling_im = PhotoImage(file=relative_to_assets_2("7.png"))
    filling_btn = Button(
        image=filling_im,
        borderwidth=0,
        highlightthickness=0,
        bg="#D9D9D9",
        activebackground="#D9D9D9",
        relief="flat"
    )
    filling_btn.place(x=1405.0, y=1005.0, width=50.0, height=50.0)

    window.resizable(False, False)
    window.mainloop()
main_window()
