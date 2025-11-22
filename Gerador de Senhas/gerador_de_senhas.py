import random
import string

def gerar_senha(tamanho, letra, especial, caso, numero):
    obrigatorios = []
    caracteres = ""

    if letra == "SIM":
        if caso == 1:
            caracteres += string.ascii_uppercase
            obrigatorios.append(random.choice(string.ascii_uppercase))
        elif caso == 2:
            caracteres += string.ascii_lowercase
            obrigatorios.append(random.choice(string.ascii_lowercase))
        elif caso == 3:
            caracteres += string.ascii_letters
            obrigatorios.append(random.choice(string.ascii_letters))

    if numero == "SIM":
        caracteres += string.digits
        obrigatorios.append(random.choice(string.digits))

    if especial == "SIM":
        caracteres += string.punctuation
        obrigatorios.append(random.choice(string.punctuation))

    if not caracteres:
        return ""
    
    # if tamanho < len(obrigatorios):
    #     raise ValueError("Tamanho da senha menor que o número de " \
    #     "tipos obrigatórios.")

    senha = obrigatorios + [random.choice(caracteres) for _ in 
                            range(tamanho - len(obrigatorios))]
    random.shuffle(senha)

    return ''.join(senha)


def entrada_inteiro(msg, opcoes=None):
    while True:
        try:
            valor = int(input(msg))

            if opcoes and valor not in opcoes:
                print("Digite uma opção válida:", opcoes)
                continue
            
            return valor
        
        except ValueError:
            
            print("Digite apenas números.")

def entrada_sim_nao(msg):
    while True:
        valor = input(msg).upper().strip()

        if valor in ["SIM", "NAO"]:
            return valor
        
        print("Digite apenas 'Sim' ou 'Nao'.")

def menu():
    tamanho = entrada_inteiro("Digite o número de caracteres da sua senha: ")
    especial = entrada_sim_nao("Sua senha deverá ter caracteres especiais? "
    "(Sim/Nao): ")
    numero = entrada_sim_nao("Sua senha deverá ter números? (Sim/Nao): ")
    letra = entrada_sim_nao("Sua senha deverá ter letras? (Sim/Nao): ")
    
    caso = 0
    if letra == "SIM":
        caso = entrada_inteiro("Sua senha deverá ter maiúsculas(1), " \
        "minúsculas(2) ou os dois(3)? (1/2/3): ", [1,2,3])
    
    tipos_obrigatorios = 0
    if letra == "SIM":
        tipos_obrigatorios += 1
    if numero == "SIM":
        tipos_obrigatorios += 1
    if especial == "SIM":
        tipos_obrigatorios += 1

    while tamanho < tipos_obrigatorios:
        print(f"O tamanho mínimo da senha deve ser {tipos_obrigatorios}, pois "
              f"você escolheu {tipos_obrigatorios} tipos de caracteres.")
        tamanho = entrada_inteiro("Digite novamente o número de caracteres da "
        "sua senha: ")

    senha = gerar_senha(tamanho, letra, especial, caso, numero)
    print("Senha gerada:", senha)


menu()
