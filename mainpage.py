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

        self.hint_label = customtkinter.CTkLabel(frame1, text="", text_color="black", width=200)
        self.hint_label.pack(pady=20, padx=20)

        self.resposta_jogador = customtkinter.CTkEntry(frame1, placeholder_text="Qual é o animal? ", text_color="black")
        self.resposta_jogador.pack(pady=20, padx=20)

        self.btn_conferir = customtkinter.CTkButton(frame1, text="Conferir", command=self.answer_player, width=75, height=30, fg_color="yellow", text_color="black")
        self.btn_conferir.pack()

        label_basic = customtkinter.CTkLabel(frame1, text="")
        label_basic.pack(pady=10)

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
            "Rinoceronte": "Tem um chifre na testa, é herbívoro e vive em savanas e florestas.",
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
        animal, dica = self.random_animal()
        self.hint_label.configure(text=dica)
        print(f"O animal escolhido foi: {animal}")

    def answer_player(self, names):
        self.quantidade_max = 10
        self.quantidade_pontos_player1 = 0
        self.quantidade_pontos_player2 = 0

        player1 = {''.join(names[0])}
        player2 = {''.join(names[1])}

        resposta_certa = False

        while not resposta_certa:
            if self.resposta_jogador == self.random_animal:
                self.player1 = self.quantidade_pontos_player1 =+ 1
                print(f"O {player1} está com {self.quantidade_pontos_player1}")
            else:
                pass