from datetime import datetime
import locale
import re 

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

def validar_nome(aluno):
    if not aluno.replace(" ", "").isalpha():
        print("\nERRO: Nome do aluno deve conter apenas letras!\n")
        return False

    if not aluno.strip():
        print("\nERRO: Nome do aluno não pode ser vazio!\n")
        return False
    
    try:
        float(aluno)
        print("\nERRO: O Nome do aluno não deve conter números!\n")
        return False
    except ValueError:
        return True
    


def validar_nota(nota1,nota2):
    if  (nota1 < 0 or nota1 > 10) or (nota2 < 0 or nota2 > 10):
        print("\nERRO: Notas devem ser entre 0 e 10!\n")
        return False
    return True


def validar_data_nascimento(data_nascimento):
    if not data_nascimento.strip():
        print("\nERRO: Data de nascimento não pode ser vazia!\n")
        return None
    
    try:
        hoje = datetime.now()
        data_formatada = datetime.strptime(data_nascimento, "%d/%m/%Y")
        idade = hoje.year - data_formatada.year
        if (hoje.month, hoje.day) < (data_formatada.month, data_formatada.day):
            idade -= 1
        if idade < 12 or idade > 18:
            print("\nERRO: Idade fora do intervalo permitido (12 a 18 anos)!\n")
            return None
        
        return idade

    except ValueError:
        print("\nErro na data! Use o formato DD/MM/AAAA.\n")
        return None
    
