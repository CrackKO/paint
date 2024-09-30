from customtkinter import *
app = CTk()
app.geometry("500x400")
set_appearance_mode("dark")
btn = CTkButton(master=app,text="Create",corner_radius=32,fg_color="#C850C0",hover_color="#4158D0",
                font=("Lexend",20))
btn.place(relx= 0.5, rely=0.6, anchor = "center")
btn2 = CTkButton(master=app,text="Open",corner_radius=32,fg_color="#C850C0",hover_color="#4158D0",
                font=("Lexend",20))
btn2.place(relx= 0.5, rely=0.5, anchor = "center")
checkbox= CTkCheckBox(master=app,text="Dark Mode", fg_color="#C850C0",checkbox_height=20,checkbox_width=20,corner_radius=36)
checkbox.place(relx = 0.5, rely = 0.7, anchor = "center")
print("Helloworld")
app.mainloop()
