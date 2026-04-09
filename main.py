from sistema import entrada, estatisticas, organização, processamento, relatorio, validacão

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
        print("\n[ERRO] Digite apenas números")
        continue 

    match menu:
        case 1:
            nome = entrada.obter_nome()

            if not validacão.validar_nome(nome):
                continue
            
            data_nascimento = entrada.obter_data_nascimento()

            idade = validacão.validar_data_nascimento(data_nascimento)

            if idade is None:
                continue

            try:
                nota1, nota2 = entrada.obter_nota()
            except ValueError:
                print("\n[ERRO] Notas devem ser números.\n")
                continue
            

            if not validacão.validar_nota(nota1, nota2):
                continue
            
            media = processamento.calcular_media(nota1, nota2)
            status = processamento.classificar_aluno(media)

            processamento.cria_aluno(nome, data_nascimento, idade, nota1, nota2, media, status, lista_alunos)

        case 2:
            organização.listar_alunos(lista_alunos)
            

        case 3: 
            estatisticas.mostrar_estatisticas(lista_alunos)
        
        case 4:
            relatorio.gerar_excel(lista_alunos)
            
        case 0:
            print("\nSaindo...")
            break
        
        case _:
            print("\n[AVISO] Opção inválida! Escolha entre 1 e 4 ou 0.")