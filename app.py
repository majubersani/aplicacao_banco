from flask import Flask, render_template, request, redirect, url_for, flash
from sqlalchemy import select
from models import db_session, Veterinario, Cliente, Animal, Produto

app = Flask(__name__)
app.config[('SECRET_KEY')] = 'secret!'

@app.route('/')
def inicial():
    return render_template('inicio.html')


@app.route('/gerenciamento')
def gerenciamento():
    return render_template('gerenciamento.html')


@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

#cliente
@app.route('/cadastro_cliente', methods=['GET','POST'])
def cadastro_cliente():
    if request.method == 'POST':
        if (not request.form['CPF']or not request.form['nome']or not request.form['telefone']or not
        request.form['profissao']or not request.form['area']):
            flash('Preecha todos os campos!')
        else:
            cadastro_cliente = Cliente(CPF=request.form['CPF'],
                                       Nome=request.form['nome'],
                                       telefone=request.form['telefone'],
                                       Profissao=request.form['profissao'],
                                       Area=request.form['area']
                                       )
            print(cadastro_cliente)
            cadastro_cliente.save()
            db_session.close()
            flash('Cliente cadastrado com sucesso!')
            return redirect('cadastro')
    return render_template('cadastro_cliente.html')

#animal
@app.route('/cadastroanimal', methods=['GET' , 'POST'])
def cadastro_animal():
    if request.method == 'POST':
        if (not request.form['nome_animal']or not request.form['raca']or not request.form['anoNasci']):
            flash('Preencha todos os campos!')
        else:
            cadastro_animal = Animal(nome_animal=request.form['nome_animal'],
                                     raca=request.form['raca'],
                                     anoNasci=request.form['anoNasci'])
            print(cadastro_animal)
            cadastro_animal.save()
            db_session.close()
            flash('Animal cadastrado com sucesso!')
            return redirect(url_for('cadastro'))
    return render_template('cadastro_animal.html')


#veterinario
@app.route('/cadastroveterinario', methods=['GET','POST'])
def cadastro_veterinario1():
    if request.method == 'POST':
        if (not request.form['salario']or not request.form['nomeVet']or not request.form['crmv']or not request.form['v_consulta']):
            flash('Preencha todos os campos!')
        else:
            cadastro_veterinario = Veterinario(
                salario=request.form['salario'],
                nomeVet=request.form['nomeVet'],
                crmv=request.form['crmv'],
                v_consulta=request.form['v_consulta']
            )
            print(cadastro_veterinario)
            cadastro_veterinario.save()
            db_session.close()
            flash('Veterinário cadastrado com sucesso!')
            return redirect(url_for('cadastro'))
    return render_template('cadastro_veterinario.html')


#produto
@app.route('/cadastroproduto', methods=['GET','POST'])
def cadastro_produto1():
    if request.method == 'POST':
        if (not request.form['nome_produto']or not request.form['PRECO']or not request.form['cat_produto']):
            flash('Preencha todos os campos!')
        else:
            cadastro_produto = Produto(
                nome_produto=request.form['nome_produto'],
                PRECO=request.form['PRECO'],
                cat_produto=request.form['cat_produto'],
            )
            print(cadastro_produto)
            cadastro_produto.save()
            db_session.close()
            flash('Produto cadastrado com sucesso')
            return redirect(url_for('cadastro'))
    return render_template('cadastro_produto.html')

if __name__ == '__main__':
    app.run(debug=True)
