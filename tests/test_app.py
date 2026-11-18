from app import create_app


def test_pagina_inicial_carrega():
    app = create_app()
    app.config.update(TESTING=True)
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert "Futebol Social" in response.get_data(as_text=True)


def test_formulario_de_cadastro_carrega():
    app = create_app()
    app.config.update(TESTING=True)
    response = app.test_client().get("/alunos/novo")

    assert response.status_code == 200
    assert "Cadastrar aluno" in response.get_data(as_text=True)


def test_cadastro_com_dados_invalidos_nao_e_aceito():
    app = create_app()
    app.config.update(TESTING=True)
    response = app.test_client().post(
        "/alunos/novo",
        data={
            "nome": "",
            "data_nascimento": "data-invalida",
            "nome_responsavel": "",
            "telefone": "",
            "email": "",
        },
    )

    assert response.status_code == 400
    assert "Informe o nome do aluno." in response.get_data(as_text=True)


def test_cadastro_valido_exibe_aviso_de_etapa():
    app = create_app()
    app.config.update(TESTING=True)
    response = app.test_client().post(
        "/alunos/novo",
        data={
            "nome": "Aluno de Teste",
            "data_nascimento": "2013-03-15",
            "nome_responsavel": "Responsavel de Teste",
            "telefone": "11999999999",
            "email": "teste@example.com",
        },
        follow_redirects=True,
    )

    assert response.status_code == 200
    assert "Dados validados!" in response.get_data(as_text=True)
