##  ❌🤖 Aplicação

<p>A aplicação desenvolvida se trata de um simples formulário que realiza o cadastro de um usuário, permitindo que seja possível fazer um login e redirecionando para uma tela de perfil.</p>
<p>Tudo no intuito de explicar a integração de um formulário com o Google reCAPTCHA!</p>

## 🤔 Como rodar

- Faça o download desse repositório;
- Instale e ative sua virtualenv: `python -m venv venv`  `venv/scripts/activate` ou `venv/bin/activate`;
- Instale as dependências: `pip install -r requirements.txt`;
- <b>Ajuste as suas reCaptcha Keys nos arquivos:</b> `pycaptcha/blueprints/views.py`, `pycaptcha/blueprints/templates/login.html` e `pycaptcha/blueprints/templates/cadastrar.html`
- Crie o banco de dados: `flask create-db`;
- Por fim, execute: `flask run`;
- Caso queira dar um drop no banco já existente, execute: `flask drop-db`.

## 🧰 Tecnologias

Essa aplicação foi desenvolvida com [Python](https://docs.python.org/pt-br/3/index.html) e suas seguintes bibliotecas:

- [Requests](https://requests.readthedocs.io/en/latest/)
- [Flask](https://flask.palletsprojects.com/en/1.1.x/)
- [Flask-Login](https://flask-login.readthedocs.io/en/latest/)
- [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)
- [Dynaconf](https://dynaconf.readthedocs.io/en/latest/)

## 📝 Observações

- Vídeo explicação da aplicação desenvolvida: [Vídeo](https://www.youtube.com/watch?v=fsXAjdGuT5Y)
