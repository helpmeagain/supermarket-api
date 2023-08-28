from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


# Criando o banco
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///clientes.db'
db = SQLAlchemy(app)

class Cliente(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  nome = db.Column(db.String(100))
  cpf = db.Column(db.String(11))
  nascimento = db.Column(db.String(11))
  email = db.Column(db.String(100))
  telefone = db.Column(db.String(20))

# Rota inicial
@app.route('/')
def index():
  return render_template('index.html')

# Roda de cadastro
@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
  if request.method == 'POST':
    nome = request.form['nome']
    cpf = request.form['cpf']
    email = request.form['email']
    telefone = request.form['telefone']
    nascimento = request.form['nascimento']

    cliente = Cliente(
      nome=nome,
      email=email,
      telefone=telefone,
      cpf=cpf,
      nascimento=nascimento
    )

    db.session.add(cliente)
    db.session.commit()

    return redirect(url_for('clientes'))
  else:
    return render_template('cadastro.html')

# Rota de clientes
@app.route('/clientes')
def clientes():
  clientes = Cliente.query.all()
  return render_template('clientes.html', clientes=clientes)

# SObre o cliente
@app.route('/sobre/<int:id>')
def sobre(id):
  cliente = Cliente.query.get(id)
  return render_template('sobre.html', cliente=cliente)

# Alterar ou excluir cliente
@app.route('/alteracao/<int:id>')
def alteracao(id):
  cliente = Cliente.query.get(id)
  return render_template('alteracao.html', cliente=cliente)

# Editar cliente
@app.route('/alteracao/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    cliente = Cliente.query.get(id)
    if request.method == 'POST':
        cliente.nome = request.form['nome']
        cliente.cpf = request.form['cpf']
        cliente.email = request.form['email']
        cliente.telefone = request.form['telefone']
        cliente.nascimento = request.form['nascimento']
        db.session.commit()
        return redirect(url_for('clientes'))
    else:
        return render_template('editar.html', cliente=cliente)

# Excluir o cliente
@app.route('/alteracao/excluir/<int:id>', methods=['GET', 'POST'])
def excluir(id):
  cliente = Cliente.query.get(id)
  if cliente:
    db.session.delete(cliente)
    db.session.commit()
    return redirect(url_for('clientes'))
  else:
    return render_template('clientes.html')

if __name__ == '__main__':
  with app.app_context():
    db.create_all()
    app.run(debug=True)