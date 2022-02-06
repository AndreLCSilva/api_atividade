from models import Pessoas, Usuarios

def insere_pessoas():
    pessoa = Pessoas(nome="Andre", idade=30)
    print(pessoa)
    pessoa.save()

def consulta_pessoas():
    pessoa = Pessoas.query.all()
    print(pessoa)
    pessoa = Pessoas.query.filter_by(nome="Eu").first()
    print(pessoa.idade)

def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome="Eu").first()
    pessoa.idade = 40
    pessoa.save()

def exlui_pessoa():
    pessoa = Pessoas.query.filter_by(nome="Andre").first()
    pessoa.delete()

def insere_usuario(login, senha):
    usuario = Usuarios(login=login, senha=senha)
    usuario.save()

def consulta_usuarios():
    usuarios = Usuarios.query.all()
    print(usuarios)

if __name__ == '__main__':
    #insere_pessoas()
    #altera_pessoa()
    #exlui_pessoa()
    #consulta_pessoas()
    insere_usuario('Eu', '123')
    insere_usuario('Jose', '1234')
    consulta_usuarios()
