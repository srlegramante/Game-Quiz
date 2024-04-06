#advinhe o animal correto! um animal aleatorio irá aparecer em sua tela com uma dica e você tentará acerta-lo.
import random
import time

#dicionário com keys e descrições
animais = {
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

def mensagem_apoio_acertos():
    if quantidade_de_acertos == 5:
        print("Uau! você já acertou 5 dicas de animais, será que consegue chegar em 10 acertos?")
    elif quantidade_de_acertos >=10:
        print("Parece que temos um expert com animais em!")
    else:
        pass

def mensagem_apoio_erros():
    if quantidade_de_erros == 5:
        print("Não desanime! errando que se aprende...")
    elif quantidade_de_erros >=10:
        print("Eita! caso não conheça os animais citados a cima, não desanime, apenas pesquise um pouco sobre o assunto.")

#contador de pontos
quantidade_de_erros = 0
quantidade_de_acertos = 0

resposta_certa = False

while not resposta_certa:
    animal_aleatorio = random.choice(list(animais.keys()))
    print("Um animal aleatorio irá aparecer, tente advinha-lo!")
    time.sleep(2)
    print(animais[animal_aleatorio])

    escolha = input("Qual é o animal da dica?: ").strip()

    
    if escolha.capitalize() == animal_aleatorio:
        print("Parabéns, você acertou!")
        quantidade_de_acertos += 1
        mensagem_apoio_acertos()
        continuar = input("Deseja continuar a jogar?: (Digite 1 para Sim e 2 para Não): ")
        if continuar == '1':
            resposta_certa = False
        else:
            resposta_certa = True
    else:
        print("Você errou! Tente novamente.\n")
        quantidade_de_erros += 1
        mensagem_apoio_erros()

    if quantidade_de_erros == 10:
        resposta_certa = True




print("Fim do jogo meu nobre.")
print(f"Sua quantidade de erros são {quantidade_de_erros} erros.")
print(f"Sua quantidade de acertos são = {quantidade_de_acertos} acertos.")