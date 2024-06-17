import customtkinter
from mainpage import MainPage
from PIL import Image, ImageTk

class IntroApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("500x500")
        self.root.title("Animals")
        self.root.iconbitmap('./img/gamer.ico')

        frame = customtkinter.CTkFrame(self.root, width=300, height=200, corner_radius=10)
        frame.pack(padx=20, pady=20)

        label_basic = customtkinter.CTkLabel(frame, text="Label Básica", font=("Arial bold", 30), corner_radius=15)
        label_basic.pack(pady=10)


        self.root.after(2000, self.show_main_window)

    def show_main_window(self):
        self.root.destroy()
        intro_root = customtkinter.CTk()
        MainPage(intro_root)
        intro_root.mainloop()

    
if __name__ == "__main__":
    root = customtkinter.CTk()
    app = IntroApp(root)
    root.mainloop()