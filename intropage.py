import customtkinter
from mainpage import MainPage

class IntroApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("500x500")
        self.root.title("Animais")
        self.root.iconbitmap('./img/gamer.ico')

        self.frame = customtkinter.CTkFrame(self.root, width=300, height=300, corner_radius=10, fg_color="#FFFFFF")
        self.frame.pack(padx=20, pady=20)

        self.label_basic = customtkinter.CTkLabel(self.frame, text="Digite seus nomes e vamos começar!", font=("Arial bold", 18), corner_radius=15, text_color="black")
        self.label_basic.pack(pady=10)

        self.name1_entry = customtkinter.CTkEntry(self.frame, placeholder_text="Digite o 1° nome: ", placeholder_text_color="black", fg_color="#B0C4DE", text_color="black")
        self.name1_entry.pack(pady=30)

        self.name2_entry = customtkinter.CTkEntry(self.frame, placeholder_text="Digite o 2° nome: ", placeholder_text_color="black", fg_color="#B0C4DE", text_color="black")
        self.name2_entry.pack(pady=50)

        self.btn_ready = customtkinter.CTkButton(self.frame, text="Pronto!", border_spacing=5, command=self.event)
        self.btn_ready.pack()

        self.label_basic = customtkinter.CTkLabel(self.frame, text="")
        self.label_basic.pack(pady=10)

        self.error_label = customtkinter.CTkLabel(self.frame, text="", text_color="red")
        self.error_label.pack(pady=10)

        self.names_list = []

    def event(self):
        if self.verify_names():
            self.set_names()
            self.root.destroy()
            mainpage = customtkinter.CTk()
            MainPage(mainpage, self.names_list)
            mainpage.mainloop()
        else:
            self.error_label.configure(text="Por favor, insira caracteres válidos.")

    def verify_names(self):
        invalid_chars = set('#!"$%¨&*()-_=]')
        user1 = self.name1_entry.get()
        user2 = self.name2_entry.get()
        
        if any(char in invalid_chars for char in user1) or any(char in invalid_chars for char in user2):
            return False
        return True

    def set_names(self):
        user1 = self.name1_entry.get()
        user2 = self.name2_entry.get()

        self.names_list = [user1, user2]

if __name__ == "__main__":
    root = customtkinter.CTk()
    app = IntroApp(root)
    root.mainloop()
