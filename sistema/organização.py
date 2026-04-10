def listar_alunos(lista_alunos):
    if not lista_alunos:
        print("\nNão foi cadastrado nenhum aluno!\n")
        return
    print('\n-'*20)
    print("-LISTA DE ALUNOS -")
    print('-'*20)
    for cadastro in lista_alunos:
        print(f"Aluno: {cadastro['aluno']}\n"
              f"Data de nascimento:{cadastro['data_nascimento']}\n"
              f"Idade:{cadastro['idade']}\n" 
              f"N1: {cadastro['n1']} | N2: {cadastro['n2']}\n"
              f"Média:{cadastro['media']:.2f}\n"
              f"Situação:{cadastro['status']}\n")
        
def separar_alunos(lista_alunos):
    aprovados = []
    reprovados = []
    
    for cadastro in lista_alunos:
        if cadastro['status'] == "APROVADO":
            aprovados.append(cadastro)
        else:
            reprovados.append(cadastro)

    return aprovados, reprovados
            
