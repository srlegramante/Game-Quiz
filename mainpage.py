import customtkinter

class MainPage:
    def __init__(self, root):
        self.root = root
        self.root.geometry("500x500")
        self.root.title("Animals")
        self.root.iconbitmap('./img/gamer.ico')

        frame1 = customtkinter.CTkFrame(self.root, width=150, height=150, corner_radius=10)
        frame1.pack(pady= 20, padx= 20)

        label1 = customtkinter.CTkLabel(frame1, text=f"Olá jogadores {self.buscar_nomes}")
        label1.pack(pady=20, padx=20)

        label1 = customtkinter.CTkLabel(frame1, text="Um animal aleatorio irá aparecer, tente advinha-lo!")
        label1.pack(pady=20, padx=20)

    def buscar_nomes(self):
        from intropage import IntroApp
        nomes = IntroApp.names()
        print(nomes)