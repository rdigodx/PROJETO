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
            while True:
                nome = entrada.obter_nome()
                if validacao.validar_nome(nome):
                    break

            while True:
                data_nascimento = entrada.obter_data_nascimento()
                idade = validacao.validar_data_nascimento(data_nascimento)
                if idade is not None:
                    break

            while True:
                try:
                    nota1, nota2 = entrada.obter_nota()
                except ValueError:
                    print("\n[ERRO] Notas devem ser números.\n")
                    continue

                if validacao.validar_nota(nota1, nota2):
                    break

            media = processamento.calcular_media(nota1, nota2)
            status = processamento.classificar_aluno(media)

            processamento.cria_aluno(nome, data_nascimento, idade, nota1, nota2, media, status, lista_alunos)

        case 2:
            if not lista_alunos:
                print("\nNão foi cadastrado nenhum aluno!\n")
                continue
            
            organizacao.listar_alunos(lista_alunos)
            

        case 3: 
            print('='*40)
            print("      - ESTATÍSTICAS -  ")
            print('='*40)

            if not lista_alunos:
                print("\nNão há alunos cadastrados para mostrar estatísticas.\n")
                continue
            
            total_alunos = estatisticas.total_de_alunos(lista_alunos)
            print(f"\nTotal de alunos cadastrados: {total_alunos}\n")
            
            quantidade_aprovados = organizacao.separar_alunos(lista_alunos)[0]
            print(f"Quantidade de alunos aprovados: {quantidade_aprovados}\n")
            
            quantidade_reprovados = organizacao.separar_alunos(lista_alunos)[1]
            print(f"Quantidade de alunos reprovados: {quantidade_reprovados}\n")
            
            media_geral = estatisticas.media_da_turma(lista_alunos)
            print(f"\nMédia Geral da Turma: {media_geral:.2f}\n")
            
            nome_melhor, media_melhor = estatisticas.melhor_aluno(lista_alunos)
            if nome_melhor is None:
                print("Nenhum aluno cadastrado para calcular o melhor da turma.")
            else:
                print(f"O Melhor aluno da turma é: {nome_melhor} ({media_melhor:.2f})\n")
            
        
        case 4:
            if not lista_alunos:
                print("\nNão há alunos cadastrados para gerar relatórios.\n")
                continue

            aprovados, reprovados = organizacao.separar_alunos(lista_alunos)
            arquivos_gerados = []

            if aprovados:
                caminho_aprovados = relatorio.criar_planilha("aprovados.xlsx", "90EE90", aprovados)
                arquivos_gerados.append(caminho_aprovados)
            else:
                print("\nNenhum aluno aprovado. Relatório de aprovados não foi gerado.")

            if reprovados:
                caminho_reprovados = relatorio.criar_planilha("reprovados.xlsx", "FF7F7F", reprovados)
                arquivos_gerados.append(caminho_reprovados)
            else:
                print("Nenhum aluno reprovado. Relatório de reprovados não foi gerado.")

            if arquivos_gerados:
                print(f"\nRelatórios gerados com sucesso em: {', '.join(arquivos_gerados)}\n")
            
        case 0:
            print("\nSaindo...")
            break
        
        case _:
            print("\n[AVISO] Opção inválida! Escolha entre 1 e 4 ou 0.\n")
