from customtkinter import *

app = CTk()
#Создаем окно размером (...х...) и добавляем тему приложения
app.geometry("500x400")
set_appearance_mode("dark")
"""
Создаем кнопку "Create" и задаем ей сопутствующие параметры
Параметр corner_radius отвечает за скрукгление кнопки (схему работы описал ниже)
Параметр fg_color отвечает за цвет самой кнопки
Параметр hover_color отвечает за цвет кнопки при наведении
"""
btn = CTkButton(master=app,text="Create",corner_radius=32,fg_color="#C850C0",hover_color="#4158D0",
                font=("Lexend",20))
#Задаем разположение кнопки "Create". 
btn.place(relx= 0.5, rely=0.6, anchor = "center")
btn2 = CTkButton(master=app,text="Open",corner_radius=32,fg_color="#C850C0",hover_color="#4158D0",
                font=("Lexend",20))
btn2.place(relx= 0.5, rely=0.5, anchor = "center")
"""
Создаем клик-кнопку(?) и задаем ей сопутствующие параметры, изначально она квадратная. 
Параметрами checkbox_height(высота) и checkbox_width(ширина) задаем хитбокс кнопки
Параметром corner_radius задаем радиус AKA скругление нашей кнопочки :)
"""
checkbox= CTkCheckBox(master=app,text="Dark Mode", fg_color="#C850C0",checkbox_height=20,checkbox_width=20,corner_radius=36)
checkbox.place(relx = 0.5, rely = 0.7, anchor = "center")

app.mainloop()
