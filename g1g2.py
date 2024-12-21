from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage, filedialog, messagebox, Label
from customtkinter import *
import webbrowser
from tkinter import colorchooser
from tkinter import Scale
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH_1 = OUTPUT_PATH / Path(r"F:\paint\build\assets\frame0")
ASSETS_PATH_2 = OUTPUT_PATH / Path(r"F:\paint\build2\assets\frame1")
# ASSETS_PATH_1 = OUTPUT_PATH / Path(r"D:\arigato\paint\build2\assets\frame0")
# ASSETS_PATH_2 = OUTPUT_PATH / Path(r"D:\arigato\paint\build2\assets\frame1")
# ASSETS_PATH_1 = OUTPUT_PATH / Path(r"C:\ilyxa_paint\paint\build\assets\frame0")
# ASSETS_PATH_2 = OUTPUT_PATH / Path(r"C:\ilyxa_paint\paint\build2\assets\frame1")
brush_color = "black"  # Цвет по умолчанию
def relative_to_assets_1(path: str) -> Path:
    return ASSETS_PATH_1 / Path(path)

def relative_to_assets_2(path: str) -> Path:
    return ASSETS_PATH_2 / Path(path)

def gitlink():
    webbrowser.open("https://github.com/CrackKO/paint")

def dslink():
    webbrowser.open("https://discord.gg/HNuTn6jscR")

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

    def start_draw_brush(event):
        global last_x, last_y
        last_x, last_y = event.x, event.y

    def draw_brush(event):
        global last_x, last_y, brush_color
        canvas.create_line(
            last_x, last_y, event.x, event.y,
            fill=brush_color,  # Используем выбранный цвет
            width=brush_size,  # Толщина линии
            capstyle="round"  # Закругленные линии
        )
        last_x, last_y = event.x, event.y


    def start_draw_pencil(event):
            global last_x, last_y
            last_x, last_y = event.x, event.y

    def draw_pencil(event):
            global last_x, last_y
            x, y = event.x, event.y
            canvas.create_line(last_x, last_y, x, y, fill="black", width=brush_size-3)
            last_x, last_y = x, y

    def start_draw_eraser(event):
        global last_x, last_y
        last_x, last_y = event.x, event.y

    def draw_eraser(event):
        global last_x, last_y
        x, y = event.x, event.y
        canvas.create_rectangle(
            x - brush_size//2, y - brush_size//2, 
            x + brush_size//2, y + brush_size//2, 
            fill="#202020", outline="#202020")
        last_x, last_y = x, y
    def show_slider(tool):
    
        global brush_size

        def update_tool_size(value):
            """Обновить толщину текущего инструмента."""
            global brush_size
            brush_size = int(value)

        # Удаление старого ползунка, если он уже есть
        for widget in window.winfo_children():
            if isinstance(widget, Scale):
                widget.destroy()

        # Создание и отображение нового ползунка
        thickness_slider = Scale(
            window,
            from_=1,  # Минимальная толщина
            to=50,    # Максимальная толщина
            orient="horizontal",
            bg="#202020",
            fg="white",
            highlightthickness=0,
            activebackground="#404040",
            command=update_tool_size
        )
        thickness_slider.set(brush_size)
        thickness_slider.place(x=window.winfo_width() // 2 - 150, y=950, width=300)  # Центрирование по горизонтали

    def start_filling(event):
        x, y = event.x, event.y
        target_color = canvas.gettags(canvas.find_closest(x, y))[0]
        if target_color != fill_color:
            flood_filling(x, y, target_color, fill_color)

    def flood_filling(x, y, target_color, replacement_color):
        # Если цвет области уже совпадает с заменяемым, ничего не делаем
        if target_color == replacement_color:
            return

        # Используем стек для хранения пикселей, которые нужно проверить
        stack = [(x, y)]
        while stack:
            x, y = stack.pop()
            # Проверяем пиксели и заменяем цвет
            items = canvas.find_overlapping(x, y, x+1, y+1)
            for item in items:
                if target_color in canvas.gettags(item):
                    canvas.itemconfig(item, fill=replacement_color)
                    canvas.addtag_withtag(replacement_color, item)

                    # Добавляем соседние пиксели в стек
                    stack.extend([(x-1, y), (x+1, y), (x, y-1), (x, y+1)])

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
    fill_color = "#FFFFFF"
    def brush():
        global brush_color
        color = colorchooser.askcolor(title="Выберите цвет")[1]
        brush_color = color if color else "black"

        show_slider("brush")

        canvas.bind("<Button-1>", start_draw_brush)
        canvas.bind("<B1-Motion>", draw_brush)



    
    def pencil():
        global brush_color
        color = colorchooser.askcolor(title="Выберите цвет")[1]
        brush_color = color if color else "black"
        show_slider("pencil") 
        canvas.bind("<Button-1>", start_draw_pencil)
        canvas.bind("<B1-Motion>", draw_pencil)

   
    def eraser():
        show_slider("eraser") 

        canvas.bind("<Button-1>", start_draw_eraser)
        canvas.bind("<B1-Motion>", draw_eraser)


    def filling():
        canvas.bind("<Button-3>", start_filling)  # Заливка правой кнопкой мыши
    def add_text():
        def start_text_input(event):
            x, y = event.x, event.y

            # Поле для ввода текста
            entry = CTkEntry(window, width=200)
            entry.place(x=x, y=y)

            def place_text(event=None):
                # Получение текста из Entry
                text = entry.get()
                if text:
                    # Добавление текста на Canvas
                    text_id = canvas.create_text(x, y, text=text, fill=brush_color, font=("Arial", 16), anchor="nw")
                    canvas.tag_bind(text_id, "<Button-1>", lambda e, id=text_id: edit_or_delete_text(e, id))
                entry.destroy()  # Удаление поля ввода

            # Подтверждение ввода текста при нажатии Enter
            entry.bind("<Return>", place_text)
            entry.focus()

        def edit_or_delete_text(event, text_id):
            def delete_text():
                canvas.delete(text_id)
                popup.destroy()

            def edit_text():
                text_coords = canvas.coords(text_id)
                current_text = canvas.itemcget(text_id, "text")
                canvas.delete(text_id)

                # Восстановление поля ввода для редактирования
                entry = CTkEntry(window, width=200)
                entry.place(x=text_coords[0], y=text_coords[1])
                entry.insert(0, current_text)

                def place_edited_text(event=None):
                    new_text = entry.get()
                    if new_text:
                        new_text_id = canvas.create_text(
                            text_coords[0], text_coords[1], text=new_text, fill=brush_color, font=("Arial", 16), anchor="nw"
                        )
                        canvas.tag_bind(new_text_id, "<Button-1>", lambda e, id=new_text_id: edit_or_delete_text(e, id))
                    entry.destroy()

                entry.bind("<Return>", place_edited_text)
                entry.focus()

            # Создание всплывающего меню для выбора действия
            popup = CTkToplevel(window)
            popup.geometry("200x100")
            popup.title("Действие")
            popup.configure(bg="#202020")

            delete_btn = CTkButton(popup, text="Удалить", command=delete_text)
            delete_btn.pack(pady=10)

            edit_btn = CTkButton(popup, text="Редактировать", command=edit_text)
            edit_btn.pack(pady=10)

        # Связываем действие выбора места для текста
        canvas.bind("<Button-1>", start_text_input)

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
        command=brush
    )
    brush_btn.place(x=505.0, y=1005.0, width=50.0, height=50.0)

    pencil_im = PhotoImage(file=relative_to_assets_2("2.png"))
    pencil_btn = Button(
        image=pencil_im,
        borderwidth=0,
        highlightthickness=0,
        bg="#D9D9D9",
        activebackground="#D9D9D9",
        relief="flat",
        command=pencil
    )
    pencil_btn.place(x=655.0, y=1005.0, width=50.0, height=50.0)

    eraser_im = PhotoImage(file=relative_to_assets_2("3.png"))
    eraser_btn = Button(
        image=eraser_im,
        borderwidth=0,
        highlightthickness=0,
        bg="#D9D9D9",
        activebackground="#D9D9D9",
        relief="flat",
        command=eraser
    )
    eraser_btn.place(x=805.0, y=1005.0, width=50.0, height=50.0)

    ely_logo_im = PhotoImage(file=relative_to_assets_2("4.png"))
    ely_logo_btn = Button(
        image=ely_logo_im,
        borderwidth=0,
        highlightthickness=0,
        bg="#D9D9D9",
        command=dslink,
        activebackground="#D9D9D9",
        relief="flat"
    )
    ely_logo_btn.place(x=955.0, y=1005.0, width=50.0, height=50.0)
    
    
    txt_im = PhotoImage(file=relative_to_assets_2("5.png"))
    txt_btn = Button(
        image=txt_im,
        borderwidth=0,
        highlightthickness=0,
        bg="#D9D9D9",
        activebackground="#D9D9D9",
        relief="flat"
    )
    txt_btn.configure(command=add_text)
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
        relief="flat",
        command=filling
    )
    filling_btn.place(x=1405.0, y=1005.0, width=50.0, height=50.0)

    tk_textbox = CTk.CTkTextbox(CTk, activate_scrollbars=False)
    tk_textbox.grid(row=0, column=0, sticky="nsew")
    ctk_textbox_scrollbar = CTk.CTkScrollbar(CTk, command=tk_textbox.yview)
    ctk_textbox_scrollbar.grid(row=0, column=1, sticky="ns")

    window.resizable(False, False)
    window.mainloop()
main_window()
