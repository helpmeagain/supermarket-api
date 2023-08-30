from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


# Criando o banco
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///produtos.db'
db = SQLAlchemy(app)

class produto(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  nome = db.Column(db.String(100))
  fabricante = db.Column(db.String(11))
  categoria = db.Column(db.String(11))
  quantidade = db.Column(db.String(100))
  preço = db.Column(db.String(20))

# Rota inicial
@app.route('/')
def index():
  return render_template('index.html')

# Roda de cadastro
@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
  if request.method == 'POST':
    nome = request.form['nome']
    fabricante = request.form['fabricante']
    categoria = request.form['categoria']
    quantidade = request.form['quantidade']
    preço = request.form['preço']

    produto = Produto(
      nome=nome,
      fabricante=fabricante,
      categoria=categoria,
      quantidade=quantidade,
      preço=preço
    )

    db.session.add(produto)
    db.session.commit()

    return redirect(url_for('produtos'))
  else:
    return render_template('cadastro.html')

# Rota de produtos
@app.route('/produtos')
def produtos():
  produtos = Produto.query.all()
  return render_template('produtos.html', produtos=produtos)

# SObre o produto
@app.route('/sobre/<int:id>')
def sobre(id):
  produto = produto.query.get(id)
  return render_template('sobre.html', produto=produto)

# Alterar ou excluir produto
@app.route('/alteracao/<int:id>')
def alteracao(id):
  produto = Produto.query.get(id)
  return render_template('alteracao.html', produto=produto)

# Editar produto
@app.route('/alteracao/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    produto = Produto.query.get(id)
    if request.method == 'POST':
        produto.nome = request.form['nome']
        produto.fabricante = request.form['fabricante']
        produto.categoria = request.form['categoria']
        produto.quantidade = request.form['quantidade']
        produto.preço = request.form['preço']
        db.session.commit()
        return redirect(url_for('produtos'))
    else:
        return render_template('editar.html', produto=produto)

# Excluir o produto
@app.route('/alteracao/excluir/<int:id>', methods=['GET', 'POST'])
def excluir(id):
  produto = Produto.query.get(id)
  if produto:
    db.session.delete(produto)
    db.session.commit()
    return redirect(url_for('produtos'))
  else:
    return render_template('produtos.html')

if __name__ == '__main__':
  with app.app_context():
    db.create_all()
    app.run(debug=True)