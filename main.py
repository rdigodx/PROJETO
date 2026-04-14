from sistema import entrada, estatisticas, organização, processamento, relatorio, validacao

lista_alunos = []

print('='*40)
print("      - SISTEMA DE ALUNOS -  ")
print('='*40)


while True:
    try:
        menu = int(input(
            """1 - Cadastrar aluno
2 - Listar alunos
3 - Mostrar estatisticas
4 - Gerar relatorios (Excel)
0 - Sair
Escolha uma opção: """))
    except ValueError:
        print("\n[ERRO] Digite apenas números\n")
        continue 

    match menu:
        case 1:
            nome = entrada.obter_nome()

            if not validacao.validar_nome(nome):
                continue
            
            data_nascimento = entrada.obter_data_nascimento()

            idade = validacao.validar_data_nascimento(data_nascimento)

            if idade is None:
                continue

            try:
                nota1, nota2 = entrada.obter_nota()
            except ValueError:
                print("\n[ERRO] Notas devem ser números.\n")
                continue
            

            if not validacao.validar_nota(nota1, nota2):
                continue

            media = processamento.calcular_media(nota1, nota2)
            status = processamento.classificar_aluno(media)

            processamento.cria_aluno(nome, data_nascimento, idade, nota1, nota2, media, status, lista_alunos)

        case 2:
            organização.listar_alunos(lista_alunos)
            

        case 3: 
            print('\n='*40)
            print("      - SISTEMA DE ALUNOS -  ")
            print('=\n'*40)
            
            media_geral = estatisticas.media_da_turma(lista_alunos)3
            print(f"Média Geral da Turma: {media_geral}")
            
            melhor_aluno = estatisticas.melhor_aluno(media, lista_alunos)
            print(f"O Melhor aluno da turma é: {melhor_aluno}")
            
        
        case 4:
         reprovados = organização.separar_alunos(lista_alunos)
         aprovados = organização.separar_alunos(lista_alunos)
         relatorio.criar_planilha("aprovados.xlsx", "90EE90", aprovados)
         relatorio.criar_planilha("reprovados.xlsx", "FF7F7F", reprovados)
            
        case 0:
            print("\nSaindo...")
            break
        
        case _:
            print("\n[AVISO] Opção inválida! Escolha entre 1 e 4 ou 0.\n")