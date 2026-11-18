import os

from flask import Flask, render_template


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = os.getenv(
        "SECRET_KEY", "chave-local-nao-utilizar-em-producao"
    )

    @app.get("/")
    def inicio():
        return render_template("index.html")

    return app


app = create_app()


if __name__ == "__main__":
    app.run(debug=os.getenv("FLASK_DEBUG") == "1")
