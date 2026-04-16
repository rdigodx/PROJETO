from sistema import entrada, estatisticas, organizacao, processamento, relatorio, validacao

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
            organizacao.listar_alunos(lista_alunos)
            

        case 3: 
            print('='*40)
            print("      - SISTEMA DE ALUNOS -  ")
            print('='*40)
            
            media_geral = estatisticas.media_da_turma(lista_alunos)
            print(f"Média Geral da Turma: {media_geral:.2f}\n")
            
            nome_melhor, media_melhor = estatisticas.melhor_aluno(lista_alunos)
            if nome_melhor is None:
                print("Nenhum aluno cadastrado para calcular o melhor da turma.")
            else:
                print(f"O Melhor aluno da turma é: {nome_melhor} ({media_melhor:.2f})")
            
        
        case 4:
            if not lista_alunos:
                print("\nNão há alunos cadastrados para gerar relatórios.\n")
                continue

            aprovados, reprovados = organizacao.separar_alunos(lista_alunos)
            arquivos_gerados = []

            if aprovados:
                relatorio.criar_planilha("aprovados.xlsx", "90EE90", aprovados)
                arquivos_gerados.append("aprovados.xlsx")
            else:
                print("\nNenhum aluno aprovado. Relatório de aprovados não foi gerado.")

            if reprovados:
                relatorio.criar_planilha("reprovados.xlsx", "FF7F7F", reprovados)
                arquivos_gerados.append("reprovados.xlsx")
            else:
                print("Nenhum aluno reprovado. Relatório de reprovados não foi gerado.")

            if arquivos_gerados:
                print(f"\nRelatórios gerados com sucesso.\n")
            
        case 0:
            print("\nSaindo...")
            break
        
        case _:
            print("\n[AVISO] Opção inválida! Escolha entre 1 e 4 ou 0.\n")
