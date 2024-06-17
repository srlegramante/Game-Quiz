import tkinter as tk
import customtkinter as ctk

# Cria a janela principal
root = ctk.CTk()

# Configura o tema (opcional)
ctk.set_appearance_mode("dark")  # Modo escuro
ctk.set_default_color_theme("blue")  # Tema azul

# Define a cor de fundo da janela principal
root.configure(bg="gray20")

# Cria um frame para conter as labels (opcional, dependendo da sua necessidade)
frame = ctk.CTkFrame(master=root, width=300, height=200, corner_radius=10)
frame.pack(padx=20, pady=20)

# Label básica
label_basic = ctk.CTkLabel(master=frame, text="Label Básica")
label_basic.pack(pady=10)

# Label personalizada com fonte e tamanho
label_custom_font = ctk.CTkLabel(
    master=frame, text="Label com Fonte Customizada", font=("Arial", 20)
)
label_custom_font.pack(pady=10)

# Label personalizada com cor de texto
label_custom_color = ctk.CTkLabel(
    master=frame, text="Label com Cor de Texto", text_color="yellow"
)
label_custom_color.pack(pady=10)

# Label personalizada com cor de fundo (não transparente)
label_bg_color = ctk.CTkLabel(
    master=frame, text="Label com Cor de Fundo", fg_color="blue"
)
label_bg_color.pack(pady=10)

# Label personalizada com canto arredondado
label_rounded_corners = ctk.CTkLabel(
    master=frame, text="Label com Cantos Arredondados", fg_color="green", corner_radius=15
)
label_rounded_corners.pack(pady=10)

# Executa a aplicação
root.mainloop()