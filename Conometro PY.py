
import time
import customtkinter as ctk

def tempo():
    hora = time.strftime('%H:%M:%S')
    
    display.configure(text=hora)
    display.after(1000,tempo)

janela = ctk.CTk()
janela.title("RELOGIO DIGITAL")
janela.geometry("400x200")
janela.resizable(False,False)

display = ctk.CTkLabel(janela,font=(callable, 90, 'bold'),bg_color='black',text_color='white')
display.pack(anchor='center',expand=True)

tempo()
janela.mainloop()