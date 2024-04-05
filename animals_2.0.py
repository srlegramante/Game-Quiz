#advinhe o animal correto! um animal aleatorio irá aparecer em sua tela com uma dica e você tentará acerta-lo.
import random
import time

animais = {
    "Elefante": "O animal possui tromba, é quadrúpede e é o animal terrestre mais pesado.",
    "Cachorro": "O animal é doméstico, costuma ser amigo do homem e tem um faro apurado.",
    "Gato": "O animal é conhecido por sua agilidade, independência e habilidade de caça.",
    "Anta": "O animal é herbívoro, tem um grande porte e vive em florestas tropicais.",
    "Camelo": "O animal possui uma corcova para armazenar água e é adaptado para viver em ambientes desérticos.",
    "Papagaio": "O animal tem capacidade de imitar sons humanos e é conhecido por sua coloração vibrante.",
    "Ornitorrinco": "O animal é um mamífero que põe ovos e tem um bico semelhante ao de um pato.",
    "Abelha": "O animal é um inseto que produz mel, tem um ferrão e vive em colônias.",
    "Dragão de comodo": "O animal é uma espécie de lagarto, é venenoso e é conhecido por sua língua bifurcada."
}

quantidade_de_erros = 0
resposta_certa = False
while not resposta_certa:
    animal_aleatorio = random.choice(list(animais.keys()))
    print("Um animal aleatorio irá aparecer, tente advinha-lo!")
    time.sleep(2)
    print(animais[animal_aleatorio])

    escolha = input("Qual é o animal da dica?: ")

    if escolha.capitalize() == animal_aleatorio:
        print("Parabéns, você acertou!")
        resposta_certa = True
    else:
        print("Você errou! Tente novamente.\n")
        quantidade_de_erros += 1

    if quantidade_de_erros == 2:
        resposta_certa = True

print("Fim do jogo meu nobre.")
print(f"Sua quantidade de erros tem o total de {quantidade_de_erros} erros.")