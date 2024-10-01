from customtkinter import *
from tkinter import filedialog, messagebox
app = CTk()
#Создаем окно размером (...х...) и добавляем тему приложения
app.geometry("1920x1080")
set_appearance_mode("dark")

#Тут короче мы мутим открытие файлов. Через добавление filedialog и messagebox от CTK.
def open():
    file_path = filedialog.askopenfilename(
        title="Откройте файл .png",
        filetypes=[("PNG", "*.png")] #Указываем тип файла который выбираем
    )
    if file_path:
        label = CTkLabel(master=app, text=f"Готово", font=("Lexend",20), text_color="#00FF00")
        label.place(relx = 0.5, rely = 0.4, anchor = "center")
    else:
        messagebox.showwarning("Нет файла", "Файл не был выбран") #В случае если ты не выбрал файл то будет эта хуйня

"""
Создаем кнопку "Create" и задаем ей сопутствующие параметры
Параметр corner_radius отвечает за скрукгление кнопки (схему работы описал ниже)
Параметр fg_color отвечает за цвет самой кнопки
Параметр hover_color отвечает за цвет кнопки при наведении
"""
btn = CTkButton(master=app,text="Create",corner_radius=64,fg_color="#B22222",hover_color="#4158D0",
                font=("Lexend",20))
#Задаем разположение кнопки "Create". 
btn.place(relx= 0.45, rely=0.45, anchor = "center")
btn2 = CTkButton(master=app,text="Open",corner_radius=64,fg_color="#B22222",hover_color="#4158D0",
                font=("Lexend",20), command=open)
btn2.place(relx= 0.55, rely=0.45, anchor = "center")
"""
Создаем клик-кнопку(?) и задаем ей сопутствующие параметры, изначально она квадратная. 
Параметрами checkbox_height(высота) и checkbox_width(ширина) задаем хитбокс кнопки
Параметром corner_radius задаем радиус AKA скругление нашей кнопочки :)
"""
#функция переключателя темы
def colorthem():
      if checkbox.get():
            set_appearance_mode("light")
      else:
            set_appearance_mode("dark")
checkbox= CTkCheckBox(master=app,text="Switch Them", fg_color="#C850C0",checkbox_height=20,checkbox_width=20,corner_radius=36,command=colorthem)
checkbox.place(relx = 0.5, rely = 0.50, anchor = "center")
app.mainloop()
