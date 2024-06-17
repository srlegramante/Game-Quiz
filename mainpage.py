import customtkinter

class MainPage:
    def __init__(self, root, names):
        self.root = root
        self.root.geometry("500x500")
        self.root.title("Animals")
        self.root.iconbitmap('./img/gamer.ico')

        frame1 = customtkinter.CTkFrame(self.root, width=150, height=150, corner_radius=10)
        frame1.pack(pady= 20, padx= 20)

        label1 = customtkinter.CTkLabel(frame1, text=f"Olá jogadores {', '.join(names)}")
        label1.pack(pady=20, padx=20)

        label2 = customtkinter.CTkLabel(frame1, text="Um animal aleatorio irá aparecer, tente advinha-lo!")
        label2.pack(pady=20, padx=20)

if __name__ == "__main__":
    root = customtkinter.CTk()
    app = MainPage(root, ["Jogador1", "Jogador2"])  # This line is just for testing purposes
    root.mainloop()