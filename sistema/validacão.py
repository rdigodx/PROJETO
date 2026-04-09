from datetime import datetime
import locale 

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

def validar_nome(aluno):

    nome = aluno.strip()

    if not nome:
        print("\nERRO: Nome inválido!\n")
        return False
    
    return True
    

def validar_nota(nota1,nota2):
    if nota1 < 0 or nota1 > 10 or nota2 < 0 or nota2 > 10: 
        print("\nERRO: Nota deve ser entre 0 e 10!")
        return False
    
    return True

def validar_data_nascimento(data_nascimento):
    try:
        hoje = datetime.now()
        data_formatada = datetime.strptime(data_nascimento, "%d/%m/%Y")
        idade = hoje.year - data_formatada.year
        if (hoje.month, hoje.day) < (data_formatada.month, data_formatada.day):
            idade -= 1
        if idade < 12 or idade > 18:
            print("\nERRO: Data de nascimento inválida!\n")
            return None
        
        return idade

    except ValueError:
        print("\nErro na data! Use o formato DD/MM/AAAA.")
        return None