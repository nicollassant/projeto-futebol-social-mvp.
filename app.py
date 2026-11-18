import os
import re
from datetime import date

from flask import Flask, flash, redirect, render_template, request, url_for


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = os.getenv(
        "SECRET_KEY", "chave-local-nao-utilizar-em-producao"
    )

    @app.get("/")
    def inicio():
        return render_template("index.html")

    @app.route("/alunos/novo", methods=["GET", "POST"])
    def novo_aluno():
        if request.method == "POST":
            nome = request.form.get("nome", "").strip()
            nascimento = request.form.get("data_nascimento", "").strip()
            nome_responsavel = request.form.get("nome_responsavel", "").strip()
            telefone = request.form.get("telefone", "").strip()
            email = request.form.get("email", "").strip()

            erros = []

            if not nome:
                erros.append("Informe o nome do aluno.")
            if not nome_responsavel:
                erros.append("Informe o nome do responsável.")
            if not telefone:
                erros.append("Informe o telefone do responsável.")

            try:
                data_nascimento = date.fromisoformat(nascimento)
                if data_nascimento >= date.today():
                    erros.append("A data de nascimento deve ser anterior a hoje.")
            except ValueError:
                erros.append("Informe uma data de nascimento válida.")

            telefone_digitos = re.sub(r"\D", "", telefone)
            if telefone and not 10 <= len(telefone_digitos) <= 13:
                erros.append("Informe um telefone válido com DDD.")

            if email and ("@" not in email or "." not in email.rsplit("@", 1)[-1]):
                erros.append("Informe um e-mail válido.")

            if erros:
                for erro in erros:
                    flash(erro, "error")
                return render_template("cadastro.html", dados=request.form), 400

            # Nesta etapa os dados são validados, mas ainda não são persistidos.
            flash(
                "Dados validados! A gravação no banco de dados será implementada na próxima etapa.",
                "success",
            )
            return redirect(url_for("novo_aluno"))

        return render_template("cadastro.html", dados={})

    return app


app = create_app()


if __name__ == "__main__":
    app.run(debug=os.getenv("FLASK_DEBUG") == "1")
