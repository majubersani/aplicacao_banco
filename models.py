# biblioteca
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import scoped_session, sessionmaker, relationship, declarative_base

# configurar base de dados
# criando conexão
engine = create_engine('sqlite:///base_vet_analise_9.sqlite3')
db_session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()


#ANIMAL
class Animal(Base):
    __tablename__ = 'TAB_ANIMAL'
    id_animal = Column(Integer, primary_key=True)
    nome_animal = Column(String(40), nullable=False, index=True)
    raca = Column(String(40), index=True)
    anoNasci = Column(Integer, index=True)
    idCliente = Column(Integer, primary_key=True)


    def __repr__(self):
        return '<Animal: {} {}>'.format(self.nome_animal, self.raca)

    # função para salvar no banco
    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

    def serialize_animal(self):
        dados_animal = {
            "ID do animal": self.id_animal,
            "Nome do animal": self.nome_animal,
            "Raça do animal": self.raca,
            "ano de nascimento do animal": self.anoNasci,
            "ID do cliente": self.idCliente
        }
        return dados_animal




#VETERINARIO
class Veterinario(Base):
    __tablename__ = 'TAB_VETERINARIO'
    id_vet = Column(Integer, primary_key=True)
    salario = Column(Float, index=True, unique=True)
    nomeVet = Column(String(100), index=True, nullable=False)
    crmv = Column(Integer, index=True)
    v_consulta = Column(Float, index=True, unique=True)

    def __repr__(self):
        return '<Veterinário: {} {}>'.format(self.id_veterinario, self.nome_veterinario)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

    def serialize_veterinario(self):
        dados_veterinario = {
            "ID do veterinario": self.id_vet,
            "Salario": self.salario,
            "Nome do veterinario": self.nomeVet,
            "CRMV do veterinario": self.crmv,
            "Valor da consulta": self.v_consulta
        }
        return dados_veterinario
# projeto pessoas que atividades





#PRODUTO
class Produto(Base):
    __tablename__ = 'TAB_PRODUTO'
    id_produto = Column(Integer, primary_key=True)
    nome_produto = Column(String(40), index=True)
    PRECO = Column(Float, index=True)
    cat_produto = Column(Integer, primary_key=True)

    def __repr__(self):
        return '<Produto: {} {}>'.format(self.id_produto, self.nome_produto)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

    def serialize_animal(self):
        dados_categoria = {
            "ID do produto": self.id_produto,
            "Nome do produto": self.nome_produto,
            "Preço do produto": self.PRECO,
            "Categoria do produto": self.cat_produto
        }
        return dados_categoria






#CLIENTE
class Cliente(Base):
    __tablename__ = 'TAB_CLIENTE'
    id_cliente = Column(Integer, primary_key=True)
    CPF = Column(String(11), index=True, unique=True)
    Nome = Column(String(100), index=True, nullable=False)
    telefone = Column(String(15), index=True, nullable=False)
    Profissao = Column(String(50), index=True)
    Area = Column(String(20), index=True)

    def __repr__(self):
        return '<Clientes: {} {}>'.format(self.Nome, self.telefone)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

    def serialize_cliente(self):
        dados_categoria = {
            "ID do cliente": self.id_cliente,
            "CPF do cliente": self.CPF,
            "Nome do cliente": self.Nome,
            "Telefone do cliente": self.telefone,
            "Profissão do cliente": self.Profissao,
            "Área do cliente":self.Area
        }








#CONSULTA
class Consulta(Base):
    __tablename__ = 'TAB_CONSULTA'
    id_consulta = Column(Integer, primary_key=True)
    motivo_id = Column(Integer, index=True, unique=True)
    hora = Column(Integer, index=True, nullable=False)
    minuto = Column(Integer, index=True, nullable=False)
    data = Column(String(20), index=True)
    idAnimal = Column(Integer, index=True)
    idVeterinario= Column(Integer, index=True)

    def __repr__(self):
        return '<CONSULTA: {} {}>'.format(self.data, self.id_consulta)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

    def serialize_consulta(self):
        dados_categoria = {
            "ID da consulta": self.id_consulta,
            "ID do motivo": self.motivo_id,
            "Hora da consulta": self.hora,
            "Minuto da consulta": self.minuto,
            "Data da consulta": self.data,
            "ID do animal": self.idAnimal,
            "ID do veterinario": self.idVeterinario
        }






#VENDA
class Venda(Base):
    __tablename__ = 'TAB_VENDA'
    id_venda = Column(Integer, primary_key=True)
    data = Column(String(10), index=True,)
    id_produto = Column(Integer, index=True, nullable=False)
    id_cliente = Column(Integer, index=True, nullable=False)
    qtd = Column(Integer, index=True, nullable=False)



    def __repr__(self):
        return '<VENDA: {} {}>'.format(self.data, self.id_venda)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

    def serialize_venda(self):
        dados_categoria = {
            "ID da venda": self.id_venda,
            "Data da venda": self.data,
            "ID do produto": self.id_produto,
            "ID do cliente": self.id_cliente,
            "Quantidade de venda": self.qtd
        }



#MOTIVO
class Motivo(Base):
    __tablename__ = 'TAB_MOTIVO'
    id_motivo = Column(Integer, primary_key=True)
    nome_motivo = Column(String(50), index=True,)
    motivo_categoria = Column(String(50), index=True,)
    valor_motivo = Column(Float, index=True, nullable=False)


    def __repr__(self):
        return '<VENDA: {} {}>'.format(self.data, self.id_venda)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

    def serialize_motivo(self):
        dados_categoria = {
            "ID do motivo": self.id_motivo,
            "Nome do motivo": self.nome_motivo,
            "Motivo da categoria": self.motivo_categoria,
            "Valor do motivo": self.valor_motivo,
        }

def init_db():
    Base.metadata.create_all(bind=engine)


if __name__ == '__main__':
     init_db()