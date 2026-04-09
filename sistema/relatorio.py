from openpyxl import Workbook
from openpyxl.styles import Font, Alignment, Border, Side, PatternFill


def criar_planilha(aprovados, reprovados, lista_alunos):
    planilha = Workbook()
    planilha_ativa = planilha.active
    planilha_ativa.title = "ALUNOS"

    cabecalho = ["Nome completo", "Nota 1", "Nota 2", "Média", "Status"]
    planilha_ativa.append(cabecalho)

    fonte_negrito = Font(bold=True)
    alinhamento = Alignment(horizontal="center", vertical="center")
    borda = Border(
        left=Side(style="thin"),
        right=Side(style="thin"),
        top=Side(style="thin"),
        bottom=Side(style="thin")
    )
    preenchimento = PatternFill(start_color=969696,
                                end_color= 969696,
                                fill_type="solid")

    for col in range(1, len(cabecalho) + 1):
        cell = planilha_ativa.cell(row=1, column=col)
        cell.font = fonte_negrito
        cell.alignment = alinhamento
        cell.border = borda
        cell.fill = preenchimento


    for linha in lista_alunos:
        planilha_ativa.append(linha)


    for row in planilha_ativa.iter_rows(min_row=2, max_row=planilha_ativa.max_row, max_col=5):
        for cell in row:
            cell.alignment = alinhamento
            cell.border = borda

    
    colunas = ["A", "B", "C", "D", "E"]
    larguras = [25, 10, 10, 10, 12]
    for col, largura in zip(colunas, larguras):
        planilha_ativa.column_dimensions[col].width = largura

    planilha.save("Planilha_alunos")

criar_planilha("aprovados.xlsx", "90EE90")
criar_planilha("reprovados.xlsx", "FF7F7F")

print("Arquivos gerados com sucesso!")