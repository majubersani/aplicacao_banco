from models import Veterinario, Animal, Consulta, Motivo, Cliente, db_session, Produto
from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError

#ANIMAL
def inserir_animal():
    try:
        nome_animal = input('Nome do animal: ').strip()
        raca = input('Raça do animal: ').strip()
        anoNasci = int(input('Ano de nascimento do animal: ').strip())
        idCliente = int(input('ID do cliente: ').strip())

        animal = Animal(
            nome_animal=nome_animal,
            raca=raca,
            anoNasci=anoNasci,
            idCliente=idCliente
        )
        animal.save()
        print('Animal inserido com sucesso.')
    except ValueError:
        print("Erro: Certifique-se de inserir valores válidos.")
    except SQLAlchemyError as e:
        print(f'Erro ao inserir animal: {e}')


def consultar_animal():
    try:
        animais = db_session.execute(select(Animal)).scalars().all()
        if animais:
            for animal in animais:
                print(animal)
        else:
            print("Nenhum animal encontrado.")
    except SQLAlchemyError as e:
        print(f'Erro ao consultar animais: {e}')


def atualizar_animal():
    try:
        id_animal = int(input('ID do animal: ').strip())
        animal = db_session.execute(
            select(Animal).where(Animal.id_animal == id_animal)).scalar_one_or_none()

        if animal:
            novo_nome = input('Novo nome (deixe vazio para não alterar): ').strip()
            nova_raca = input('Nova raça (deixe vazio para não alterar): ').strip()
            novo_ano_nascimento = input('Novo ano de nascimento (deixe vazio para não alterar): ').strip
            if novo_nome:
                animal.nome_animal = novo_nome
            if nova_raca:
                animal.raca1 = nova_raca
            if novo_ano_nascimento:
                animal.anoNasci = int(novo_ano_nascimento)

            animal.save()
            print('Animal atualizado com sucesso.')
        else:
            print('Animal não encontrado.')
    except ValueError:
        print("Erro: Certifique-se de inserir valores válidos.")
    except SQLAlchemyError as e:
        print(f'Erro ao atualizar animal: {e}')


def deletar_animal():
    try:
        id_animal = int(input('ID do animal: ').strip())
        animal = db_session.execute(
            select(Animal).where(Animal.id_animal == id_animal)).scalar_one_or_none()

        if animal:
            animal.delete()
            print(f'Animal {id_animal} foi removido com sucesso.')
        else:
            print('Animal não encontrado.')
    except SQLAlchemyError as e:
        print(f'Erro ao deletar animal: {e}')





#CLIENTE
def inserir_cliente():
    try:
        CPF = input('CPF do cliente: ').strip()
        nome = input('Nome do cliente: ').strip()
        telefone = input('Telefone do cliente: ').strip()
        profissao = input('Profissão do cliente: ').strip()
        area = input('Área do cliente: ').strip()

        cliente = Cliente(
            CPF=CPF,
            Nome=nome,
            telefone=telefone,
            Profissao=profissao,
            Area=area
        )
        cliente.save()
        print('Cliente inserido com sucesso.')
    except SQLAlchemyError as e:
        print(f'Erro ao inserir cliente: {e}')


def consultar_clientes():
    try:
        clientes = db_session.execute(select(Cliente)).scalars().all()
        if clientes:
            for cliente in clientes:
                print(cliente)
        else:
            print("Nenhum cliente encontrado.")
    except SQLAlchemyError as e:
        print(f'Erro ao consultar clientes: {e}')


def atualizar_cliente():
    try:
        id_cliente = int(input('ID do cliente: ').strip())
        cliente = db_session.execute(
            select(Cliente).where(Cliente.id_cliente == id_cliente)).scalar_one_or_none()

        if cliente:
            novo_cpf = input('Novo CPF (deixe vazio para não alterar): ').strip()
            novo_nome = input('Novo nome (deixe vazio para não alterar): ').strip()
            novo_telefone = input('Novo telefone (deixe vazio para não alterar): ').strip()
            nova_profissao = input('Nova profissão (deixe vazio para não alterar): ').strip()
            nova_area = input('Nova área (deixe vazio para não alterar): ').strip()

            if novo_cpf:
                cliente.CPF = novo_cpf
            if novo_nome:
                cliente.Nome1 = novo_nome
            if novo_telefone:
                cliente.telefone = novo_telefone
            if nova_profissao:
                cliente.Profissao_2 = nova_profissao
            if nova_area:
                cliente.Area_2 = nova_area

            cliente.save()
            print('Cliente atualizado com sucesso.')
        else:
            print('Cliente não encontrado.')
    except ValueError:
        print("Erro: Certifique-se de inserir valores válidos.")
    except SQLAlchemyError as e:
        print(f'Erro ao atualizar cliente: {e}')


def deletar_cliente():
    try:
        id_cliente = int(input('ID do cliente: ').strip())
        cliente = db_session.execute(
            select(Cliente).where(Cliente.id_cliente == id_cliente)).scalar_one_or_none()

        if cliente:
            cliente.delete()
            print(f'Cliente {id_cliente} foi removido com sucesso.')
        else:
            print('Cliente não encontrado.')
    except SQLAlchemyError as e:
        print(f'Erro ao deletar cliente: {e}')






#VETERINARIO
def inserir_veterinario():
    try:
        salario = float(input('Salário do veterinário: ').strip())
        nomeVet = input('Nome do veterinário: ').strip()
        crmv = int(input('CRM do veterinário: ').strip())
        v_consulta = float(input('Valor da consulta: ').strip())

        veterinario = Veterinario(
            salario=salario,
            nomeVet=nomeVet,
            crmv=crmv,
            v_consulta=v_consulta
        )
        veterinario.save()
        print('Veterinário inserido com sucesso.')
    except ValueError:
        print("Erro: Certifique-se de inserir valores válidos.")
    except SQLAlchemyError as e:
        print(f'Erro ao inserir veterinário: {e}')


def consultar_veterinarios():
    try:
        veterinarios = db_session.execute(select(Veterinario)).scalars().all()
        if veterinarios:
            for veterinario in veterinarios:
                print(veterinario)
        else:
            print("Nenhum veterinário encontrado.")
    except SQLAlchemyError as e:
        print(f'Erro ao consultar veterinários: {e}')


def atualizar_veterinario():
    try:
        id_veterinario = int(input('ID do veterinário: ').strip())
        veterinario = db_session.execute(
            select(Veterinario).where(Veterinario.id_veterinario == id_veterinario)).scalar_one_or_none()

        if veterinario:
            novo_salario = input('Novo salário (deixe vazio para não alterar): ').strip()
            novo_nome = input('Novo nome (deixe vazio para não alterar): ').strip()
            novo_crmv = input('Novo CRM (deixe vazio para não alterar): ').strip()
            novo_valor_consulta = input('Novo valor da consulta (deixe vazio para não alterar): ').strip()

            if novo_salario:
                veterinario.salario2 = float(novo_salario)
            if novo_nome:
                veterinario.nome_Vet = novo_nome
            if novo_crmv:
                veterinario.crmv = int(novo_crmv)
            if novo_valor_consulta:
                veterinario.v_consulta1 = float(novo_valor_consulta)

            veterinario.save()
            print('Veterinário atualizado com sucesso.')
        else:
            print('Veterinário não encontrado.')
    except ValueError:
        print("Erro: Certifique-se de inserir valores válidos.")
    except SQLAlchemyError as e:
        print(f'Erro ao atualizar veterinário: {e}')


def deletar_veterinario():
    try:
        id_veterinario = int(input('ID do veterinário: ').strip())
        veterinario = db_session.execute(
            select(Veterinario).where(Veterinario.id_veterinario == id_veterinario)).scalar_one_or_none()

        if veterinario:
            veterinario.delete()
            print(f'Veterinário {id_veterinario} foi removido com sucesso.')
        else:
            print('Veterinário não encontrado.')
    except SQLAlchemyError as e:
        print(f'Erro ao deletar veterinário: {e}')






#PRODUTO
def inserir_produto():
    try:
        nome_produto = input('Nome do produto: ').strip()
        PRECO = float(input('Preço do produto: ').strip())
        cat_produto = int(input('ID da categoria do produto: ').strip())

        produto = Produto(
            nome_produto=nome_produto,
            PRECO=PRECO,
            cat_produtos=cat_produto
        )
        produto.save()
        print('Produto inserido com sucesso.')
    except ValueError:
        print("Erro: Certifique-se de inserir valores válidos.")
    except SQLAlchemyError as e:
        print(f'Erro ao inserir produto: {e}')


def consultar_produtos():
    try:
        produtos = db_session.execute(select(Produto)).scalars().all()
        if produtos:
            for produto in produtos:
                print(produto)
        else:
            print("Nenhum produto encontrado.")
    except SQLAlchemyError as e:
        print(f'Erro ao consultar produtos: {e}')


def atualizar_produto():
    try:
        id_produto = int(input('ID do produto: ').strip())
        produto = db_session.execute(
            select(Produto).where(Produto.id_produto == id_produto)).scalar_one_or_none()

        if produto:
            novo_nome = input('Novo nome (deixe vazio para não alterar): ').strip()
            novo_preco = input('Novo preço (deixe vazio para não alterar): ').strip()
            nova_categoria_id = input('Novo ID da categoria (deixe vazio para não alterar): ').strip()

            if novo_nome:
                produto.nome_produto = novo_nome
            if novo_preco:
                produto.PRECO = float(novo_preco)
            if nova_categoria_id:
                produto.cat_produtos = int(nova_categoria_id)

            produto.save()
            print('Produto atualizado com sucesso.')
        else:
            print('Produto não encontrado.')
    except ValueError:
        print("Erro: Certifique-se de inserir valores válidos.")
    except SQLAlchemyError as e:
        print(f'Erro ao atualizar produto: {e}')


def deletar_produto():
    try:
        id_produto = int(input('ID do produto: ').strip())
        produto = db_session.execute(
            select(Produto).where(Produto.id_produto == id_produto)).scalar_one_or_none()

        if produto:
            produto.delete()
            print(f'Produto {id_produto} foi removido com sucesso.')
        else:
            print('Produto não encontrado.')
    except SQLAlchemyError as e:
        print(f'Erro ao deletar produto: {e}')

if __name__ == '__main__':
    while True:
        print('Menu')
        print('1 - Inserir produto')
        print('2 - Consultar produto')
        print('3 - Atualizar produto')
        print('4 - Deletar produto')
        print('5 - Inserir veterinário')
        print('6 - Consultar veterinário')
        print('7 - Atualizar veterinário')
        print('8 - Deletar veterinário')
        print('9 - Inserir cliente')
        print('10 - Consultar cliente')
        print('11 - Atualizar cliente')
        print('12 - Deletar cliente')
        print('13 - Inserir animal')
        print('14 - Consultar animal')
        print('15 - Atualizar animal')
        print('16 - Deletar animal')
        print('17 - Sair')

        escolha = input('Escolha: ')
        if escolha == '1':
            inserir_produto()
        elif escolha == '2':
            consultar_produtos()
        elif escolha == '3':
            atualizar_produto()
        elif escolha == '4':
            deletar_produto()
        elif escolha == '5':
            inserir_veterinario()
        elif escolha == '6':
            consultar_veterinarios()
        elif escolha == '7':
            atualizar_veterinario()
        elif escolha == '8':
            deletar_veterinario()
        elif escolha == '9':
            inserir_cliente()
        elif escolha == '10':
            consultar_clientes()
        elif escolha == '11':
            atualizar_cliente()
        elif escolha == '12':
            deletar_cliente()
        elif escolha == '13':
            inserir_animal()
        elif escolha == '14':
            consultar_animal()
        elif escolha == '15':
            atualizar_animal()
        elif escolha == '16':
            deletar_animal()
        elif escolha == '17':
            break
        else:
            print('Escolha inválida, tente novamente.')
