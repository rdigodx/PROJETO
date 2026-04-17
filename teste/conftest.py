from datetime import date

import pytest

def _data_nascimento_para_idade(anos):
    hoje = date.today()
    try:
        nascimento = hoje.replace(year=hoje.year - anos)
    except ValueError:
        nascimento = hoje.replace(month=2, day=28, year=hoje.year - anos)
    return nascimento.strftime("%d/%m/%Y")


@pytest.fixture
def data_nascimento_para_idade():
    return _data_nascimento_para_idade

@pytest.fixture
def lista_alunos_exemplo():
    return [
        {
            "aluno": "ANA",
            "data_nascimento": "10/10/2010",
            "idade": 15,
            "n1": 8.0,
            "n2": 9.0,
            "media": 8.5,
            "status": "APROVADO",
        },
        {
            "aluno": "BRUNO",
            "data_nascimento": "05/04/2011",
            "idade": 15,
            "n1": 5.0,
            "n2": 6.0,
            "media": 5.5,
            "status": "REPROVADO",
        },
        {
            "aluno": "CARLA",
            "data_nascimento": "22/11/2009",
            "idade": 16,
            "n1": 9.5,
            "n2": 8.5,
            "media": 9.0,
            "status": "APROVADO",
        },
    ]


@pytest.fixture
def lista_alunos_exemplo_valor_none():
    return [0]