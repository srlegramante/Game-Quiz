import customtkinter
import random

class MainPage:
    def __init__(self, root, names):
        self.root = root
        self.root.geometry("700x500")
        self.root.title("Animals")
        self.root.iconbitmap('./img/gamer.ico')

        frame1 = customtkinter.CTkFrame(self.root, width=150, height=150, corner_radius=10)
        frame1.pack(pady= 20, padx= 20)

        self.label1 = customtkinter.CTkLabel(frame1, text=f"Olá jogadores {' e '.join(names)}")
        self.label1.pack(pady=20, padx=20)

        label2 = customtkinter.CTkLabel(frame1, text="Um animal aleatorio irá aparecer, tente advinha-lo!")
        label2.pack(pady=20, padx=20)

        self.btn_ver_dica = customtkinter.CTkButton(frame1, text="Ver dica: ", command=self.run_game_logic)
        self.btn_ver_dica.pack(pady=20, padx=20)

        self.hint_label = customtkinter.CTkLabel(frame1, text="", text_color="yellow", width=200)
        self.hint_label.pack(pady=20, padx=20)

        self.result_label = customtkinter.CTkLabel(frame1, text="", text_color="green")
        self.result_label.pack(pady=10, padx=10)

        self.error_label = customtkinter.CTkLabel(frame1, text="", text_color="red")
        self.error_label.pack(pady=10)

        self.resposta_jogador = customtkinter.CTkEntry(frame1, placeholder_text="Qual é o animal? ", text_color="black", placeholder_text_color="black", fg_color="#B0C4DE")
        self.resposta_jogador.pack(pady=20, padx=20)

        self.btn_conferir = customtkinter.CTkButton(frame1, text="Conferir", command=self.conferir_resposta, width=75, height=30, text_color="black")
        self.btn_conferir.pack()

        self.pontos = customtkinter.CTkLabel(frame1, text="")
        self.pontos.pack(pady=20)

    def lista_animais(self):
        return {
            "Elefante": "O animal possui tromba, é quadrúpede e é o animal terrestre mais pesado.",
            "Cachorro": "O animal é doméstico, costuma ser amigo do homem e tem um faro apurado.",
            "Gato": "É rápido, caça ratos e é independente.",
            "Anta": "O animal é herbívoro, tem um grande porte e vive em florestas tropicais.",
            "Camelo": "O animal possui uma corcova para armazenar água e é adaptado para viver em ambientes desérticos.",
            "Papagaio": "O animal tem capacidade de imitar sons humanos e é conhecido por sua coloração vibrante.",
            "Ornitorrinco": "O animal é um mamífero que põe ovos e tem um bico semelhante ao de um pato.",
            "Abelha": "O animal é um inseto que produz mel, tem um ferrão e vive em colônias.",
            "Dragão de comodo": "O animal é uma espécie de lagarto, é venenoso e é conhecido por sua língua bifurcada.",
            "Panda": "É preto e branco, se alimenta de bambu e vive nas florestas da China.",
            "Tigre": "Tem listras, é um excelente caçador e vive em florestas e savanas.",
            "Golfinho": "Vive no mar, é inteligente e se comunica através de sons.",
            "Girafa": "Tem pescoço longo, come folhas de árvores altas e vive nas savanas africanas.",
            "Urso Polar": "Vive no Ártico, tem uma camada de gordura para se proteger do frio e é um excelente nadador.",
            "Rinoceronte": "Tem um chifre na testa, é herbívoro e vive em savanas e floresself.tas.",
            "Lobo": "Vive em matilhas, é um excelente caçador e se comunica através de uivos.",
            "Pinguim": "Vive na Antártida, é ótimo nadador e se desloca deslizando sobre o gelo.",
            "Macaco": "Vive em árvores, é ágil e tem habilidades para se balançar de galho em galho.",
            "Leopardo": "Tem manchas rosetas, é um excelente escalador e vive em diversas regiões da África e Ásia.",
            "Elefante Marinho": "Vive no oceano, é um excelente mergulhador e tem uma probóscide.",
            "Canguru": "Tem patas traseiras fortes, vive na Austrália e é capaz de saltar longas distâncias.",
            "Cobra": "É um réptil, tem uma língua bifurcada e é um predador.",
            "Polvo": "Vive no mar, tem tentáculos e se camufla para se proteger de predadores.",
            "Coelho": "É um roedor, tem orelhas grandes e é conhecido por se reproduzir rapidamente."
        }

    def random_animal(self):
        animais = self.lista_animais()
        animal, dica = random.choice(list(animais.items()))
        return animal, dica
    

    def run_game_logic(self):
        self.btn_ver_dica.configure(state=customtkinter.DISABLED)
        self.animal, self.dica = self.random_animal()
        self.hint_label.configure(text=self.dica)
        print(f"O animal escolhido foi: {self.animal}")

        resposta = self.resposta_jogador.get()

        if resposta == self.animal:
            self.root.after(5000, self.limpar_result)
        else:
            pass

    def conferir_resposta(self):
        resposta = self.resposta_jogador.get()

        if resposta == self.animal:
            self.result_label.configure(text="Parabéns! Você acertou, vamos para o proximo!")
            self.btn_ver_dica.configure(state=customtkinter.NORMAL)
            self.root.after(4000, self.limpar_result)
        else:
            self.result_label.configure(text_color="red")
            self.result_label.configure(text="Ops... você errou, é a vez do jogador: ")

    def limpar_result(self):
        self.result_label.configure(text="")
        self.hint_label.configure(text="")
        self.resposta_jogador.delete(0, customtkinter.END)

    def verify_resposta(self):
        invalid_chars = set('#!"$%¨&*()-_=]')

        answer = self.resposta_jogador.get()

        if any(char in invalid_chars for char in answer):
            return False
        return True
        
            