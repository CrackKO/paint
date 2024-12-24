from pathlib import Path
import tkinter as tk
from tkinter import Tk, Canvas, Button, PhotoImage, filedialog, messagebox, Label, simpledialog
from PIL import Image, ImageDraw, ImageTk
from customtkinter import *
from customtkinter import CTkEntry, CTkButton, CTkToplevel
from customtkinter import CTkSlider
from CTkColorPicker import CTkColorPicker
import customtkinter as ctk
import webbrowser
from tkinter import colorchooser, Toplevel
from tkinter import Scale
import random
from PIL import Image, ImageDraw

OUTPUT_PATH = Path(__file__).parent
# ASSETS_PATH_1 = OUTPUT_PATH / Path(r"F:\paint\build\assets\frame0")
# ASSETS_PATH_2 = OUTPUT_PATH / Path(r"F:\paint\build2\assets\frame1")
# ASSETS_PATH_1 = OUTPUT_PATH / Path(r"D:\arigato\paint\build2\assets\frame0")
# ASSETS_PATH_2 = OUTPUT_PATH / Path(r"D:\arigato\paint\build2\assets\frame1")
ASSETS_PATH_1 = OUTPUT_PATH / Path(r"C:\ilyxa_paint\paint\build\assets\frame0")
ASSETS_PATH_2 = OUTPUT_PATH / Path(r"C:\ilyxa_paint\paint\build2\assets\frame1")
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
        x = event.x
        y = event.y
        for i in range(5):
            offset_x = random.randint(-brush_size // 2, brush_size // 2)
            offset_y = random.randint(-brush_size // 2, brush_size // 2)
            canvas.create_oval(
                x - brush_size // 2 + offset_x,
                y - brush_size // 2 + offset_y,
                x + brush_size // 2 + offset_x,
                y + brush_size // 2 + offset_y,
                fill=brush_color, outline=""
            )

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
        """Показать слайдер для изменения толщины инструмента."""
        global brush_size

        def update_tool_size(value):
            """Обновить толщину текущего инструмента."""
            global brush_size
            brush_size = int(value)

        # Удаление старого слайдера, если он уже есть
        for widget in window.winfo_children():
            if isinstance(widget, CTkSlider):
                widget.destroy()

        # Создание и отображение нового слайдера
        thickness_slider = CTkSlider(
            master=window,
            from_=1,  # Минимальная толщина
            to=50,    # Максимальная толщина
            command=update_tool_size
        )
        thickness_slider.place(x=window.winfo_width() // 2 - 150, y=950)

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
    canvas.grid(row=0, column=0, sticky="nsew")

    global last_x, last_y
    global brush_size
    brush_size = 5 
    fill_color = "#FFFFFF"

    def update_brush_color(color):
        global brush_color
        brush_color = color 

    def choose_brush_color():
        color_picker = CTkColorPicker(window, width=200, height=50, command=update_brush_color)
        color_picker.place(x=50, y=50)
    
    def brush():
        show_slider("brush")
        choose_brush_color()  
        canvas.bind("<Button-1>", start_draw_brush)
        canvas.bind("<B1-Motion>", draw_brush)
    
    def pencil():
        show_slider("pencil")
        choose_brush_color()  
        canvas.bind("<Button-1>", start_draw_pencil)
        canvas.bind("<B1-Motion>", draw_pencil)

    def eraser():
        show_slider("eraser") 

        canvas.bind("<Button-1>", start_draw_eraser)
        canvas.bind("<B1-Motion>", draw_eraser)

    def add_text():
        def start_text_input(event):
            
            if hasattr(window, 'popup') and window.popup.winfo_exists():
                return

            x, y = event.x, event.y

            
            entry = CTkEntry(window, width=200, corner_radius=10, border_width=2, fg_color="#2D2D2D", text_color="white")
            entry.place(x=x, y=y)

            def place_text(event=None):
                
                text = entry.get()
                if text:
                    
                    text_id = canvas.create_text(x, y, text=text, fill=brush_color, font=("Arial", 16), anchor="nw")
                    canvas.tag_bind(text_id, "<Button-1>", lambda e, id=text_id: edit_or_delete_text(e, id))
                entry.destroy()  

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

                entry = CTkEntry(window, width=200, corner_radius=10, border_width=2, fg_color="#2D2D2D", text_color="white")
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

            def choose_color():
                global brush_color 
                color = colorchooser.askcolor()[1]  
                if color:
                    brush_color = color
                    canvas.itemconfig(text_id, fill=brush_color)

            popup = CTkToplevel(window)
            popup.geometry("300x200")
            popup.title("Действие")
            popup.configure(bg="#2D2D2D")
            popup.transient(window)
            popup.grab_set()

            window.popup = popup 

            # Стилизация кнопок
            delete_btn = CTkButton(popup, text="Удалить", command=delete_text, width=200, corner_radius=10, border_width=2)
            delete_btn.pack(pady=10)

            edit_btn = CTkButton(popup, text="Редактировать", command=edit_text, width=200, corner_radius=10, border_width=2)
            edit_btn.pack(pady=10)

            color_btn = CTkButton(popup, text="Выбрать цвет", command=choose_color, width=200, corner_radius=10, border_width=2)
            color_btn.pack(pady=10)

            label = CTkLabel(popup, text="Выберите действие с текстом", text_color="white", font=("Arial", 12))
            label.pack(pady=15)

        canvas.bind("<Button-1>", start_text_input)

    bar = PhotoImage(file=relative_to_assets_2("da.png"))
    label = Label(window, background="#202020", image=bar)
    label.grid()
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

    def save_image(canvas):
        filename = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
        if not filename:
            return
        width = canvas.winfo_width()
        height = canvas.winfo_height()
        image = Image.new("RGB", (width, height), color="#171717")
        draw = ImageDraw.Draw(image)
        for item in canvas.find_all():
            if canvas.type(item) == "line":
                x1, y1, x2, y2 = canvas.coords(item)
                color = canvas.itemcget(item, "fill")
                width = canvas.itemcget(item, "width")
                width = int(float(width))
                draw.line([(x1, y1), (x2, y2)], fill=color, width=width)
            elif canvas.type(item) == "oval":
                x1, y1, x2, y2 = canvas.coords(item)
                color = canvas.itemcget(item, "fill")
                draw.ellipse([x1, y1, x2, y2], fill=color)
            elif canvas.type(item) == "rectangle":
                x1, y1, x2, y2 = canvas.coords(item)
                color = canvas.itemcget(item, "fill")
                draw.rectangle([x1, y1, x2, y2], fill=color)
            elif canvas.type(item) == "text":
                x, y = canvas.coords(item)
                text = canvas.itemcget(item, "text")
                color = canvas.itemcget(item, "fill")
                draw.text((x, y), text, fill=color)
        image.save(filename)
 
    button_save = ctk.CTkButton(
        window,
        text="Сохранить",
        command=lambda: save_image(canvas),
        width=200,
        height=50,
        corner_radius=15,
        fg_color="#4e4e4e", 
        hover_color="#202020", 
        text_color="white",
        font=("Arial", 16, "bold")
    )
    button_save.place(x=1405, y=1005)

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

    def open_shape_menu():
        # Окно для выбора фигуры
        menu_window = Toplevel(window)
        menu_window.title("Выберите фигуру")
        menu_window.geometry("300x300")
        # Функция для добавления квадрата
        def add_square():
            square = canvas.create_rectangle(100, 100, 200, 200, fill="red", outline="black")
            menu_window.destroy()  # Закрываем меню после выбора
            enable_dragging(square)  # Разрешаем перетаскивание квадрата

        # Функция для добавления круга
        def add_circle():
            circle = canvas.create_oval(100, 100, 200, 200, fill="blue", outline="black")
            menu_window.destroy()  # Закрываем меню после выбора
            enable_dragging(circle)  # Разрешаем перетаскивание круга

        # Функция для добавления линии
        def add_line():
            line = canvas.create_line(100, 100, 200, 200, fill="green", width=5)
            menu_window.destroy()  # Закрываем меню после выбора
            enable_dragging(line)  # Разрешаем перетаскивание линии

        # Функция для добавления многоугольника
        def add_polygon():
            polygon = canvas.create_polygon(150, 100, 200, 200, 100, 200, fill="purple", outline="black")
            menu_window.destroy()  # Закрываем меню после выбора
            enable_dragging(polygon)  # Разрешаем перетаскивание многоугольника

        # Функция для добавления эллипса
        def add_ellipse():
            ellipse = canvas.create_oval(100, 100, 250, 150, fill="yellow", outline="black")
            menu_window.destroy()  # Закрываем меню после выбора
            enable_dragging(ellipse)  # Разрешаем перетаскивание эллипса

        # Кнопки для выбора фигуры
        square_btn = tk.Button(menu_window, text="Квадрат", command=add_square)
        square_btn.pack(pady=5)

        circle_btn = tk.Button(menu_window, text="Круг", command=add_circle)
        circle_btn.pack(pady=5)

        line_btn = tk.Button(menu_window, text="Линия", command=add_line)
        line_btn.pack(pady=5)

        polygon_btn = tk.Button(menu_window, text="Многоугольник", command=add_polygon)
        polygon_btn.pack(pady=5)

        ellipse_btn = tk.Button(menu_window, text="Эллипс", command=add_ellipse)
        ellipse_btn.pack(pady=5)

    # Функция для разрешения перетаскивания фигуры
    def enable_dragging(item):
        # Перемещение фигуры
        def on_drag(event):
            coords = canvas.coords(item)
            if len(coords) == 4:
                x1, y1, x2, y2= coords
                canvas.coords(item, 
                              event.x - (x2 - x1) / 2, 
                              event.y - (y2 - y1) / 2, 
                              event.x + (x2 - x1) / 2, 
                              event.y + (y2 - y1) / 2)
            if len(coords) == 6:
                x1, y1, x2, y2, x3, y3 = coords
                canvas.coords(item, 
                              x1 + (event.x - ((x1 + x2 + x3) / 3)), 
                              y1 + (event.y - ((y1 + y2 + y3) / 3)), 
                              x2 + (event.x - ((x1 + x2 + x3) / 3)), 
                              y2 + (event.y - ((y1 + y2 + y3) / 3)), 
                              x3 + (event.x - ((x1 + x2 + x3) / 3)), 
                              y3 + (event.y - ((y1 + y2 + y3) / 3)))


        # Привязываем обработчик для перетаскивания
        canvas.tag_bind(item, "<Button-1>", lambda event: canvas.bind("<B1-Motion>", on_drag))

        # Функция для смены цвета фигуры при правом клике
        def change_color(event):
            color = colorchooser.askcolor()[1]  # Открываем диалог выбора цвета
            if color:
                canvas.itemconfig(item, fill=color)  # Меняем цвет фигуры
        canvas.tag_bind(item, "<Button-3>", change_color)


    shapes_im = PhotoImage(file=relative_to_assets_2("6.png"))
    shapes_btn = Button(
        image=shapes_im,
        borderwidth=0,
        highlightthickness=0,
        bg="#D9D9D9",
        activebackground="#D9D9D9",
        relief="flat",
        command=open_shape_menu
    )
    shapes_btn.place(x=1255.0, y=1005.0, width=50.0, height=50.0)


    tk_textbox = tk.Text(master=CTk)
    tk_textbox.grid(row=0, column=0, sticky="nsew")
    ctk_textbox_scrollbar = CTk.CTkScrollbar(CTk, command=tk_textbox.yview)
    ctk_textbox_scrollbar.grid(row=0, column=1, sticky="ns")

    window.resizable(False, False)
    window.mainloop()

main_window()
