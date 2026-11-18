from app import create_app


def test_pagina_inicial_carrega():
    app = create_app()
    app.config.update(TESTING=True)
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert "Futebol Social" in response.get_data(as_text=True)
    assert "aulas gratuitas de futebol" in response.get_data(as_text=True)
