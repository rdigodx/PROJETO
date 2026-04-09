def obter_nome():
    aluno = input("Digite o nome do aluno:").strip().upper()
    return aluno

def obter_data_nascimento():
    data_nascimento = input("Data de nascimento (DD/MM/AAAA):").strip()
    return data_nascimento

def obter_nota():
    nota1 = float(input("Digite a nota da N1:"))
    nota2 = float(input("Digite a nota da N2:"))
    return nota1, nota2