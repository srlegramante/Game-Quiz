import customtkinter
from mainpage import MainPage

class IntroApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("500x500")
        self.root.title("Animals")
        self.root.iconbitmap('./img/gamer.ico')

        self.frame = customtkinter.CTkFrame(self.root, width=300, height=300, corner_radius=10, fg_color="#FFFFFF")
        self.frame.pack(padx=20, pady=20)

        self.label_basic = customtkinter.CTkLabel(self.frame, text="Digite seus nomes e vamos começar!", font=("Arial bold", 18), corner_radius=15, text_color="black")
        self.label_basic.pack(pady=10)

        self.name1 = customtkinter.CTkEntry(self.frame, placeholder_text="Digite o 1° nome: ", placeholder_text_color="black", fg_color="#B0C4DE")
        self.name1.pack(pady=30)

        self.name2 = customtkinter.CTkEntry(self.frame, placeholder_text="Digite o 2° nome: ", placeholder_text_color="black", fg_color="#B0C4DE")
        self.name2.pack(pady=50)

        self.btn_pronto = customtkinter.CTkButton(self.frame, text="Pronto!", border_spacing=5, command=self.event)
        self.btn_pronto.pack()

        label_basic = customtkinter.CTkLabel(self.frame, text="")
        label_basic.pack(pady=10)

        self.error_label = customtkinter.CTkLabel(self.frame, text="", text_color="red")
        self.error_label.pack(pady=10)

        self.names_list = []

    def event(self):
        if self.verify_type_names():
            self.names()
            self.root.destroy()
            mainpage = customtkinter.CTk()
            MainPage(mainpage, self.names_list)
            mainpage.mainloop()
        else:
            self.error_label.configure(text="Por favor, digite caracteres válidos.")

    def verify_type_names(self):
        invalid_chars = set('#!"$%¨&*()-_=]')
        user1 = self.name1.get()
        user2 = self.name2.get()
        
        if any(char in invalid_chars for char in user1) or any(char in invalid_chars for char in user2):
            return False
        return True

    def names(self):
        user1 = self.name1.get()
        user2 = self.name2.get()

        self.names_list = [user1, user2]
        

if __name__ == "__main__":
    root = customtkinter.CTk()
    app = IntroApp(root)
    root.mainloop()