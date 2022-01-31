from models import Pessoas


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

if __name__ == '__main__':
    #insere_pessoas()
    #altera_pessoa()
    exlui_pessoa()
    consulta_pessoas()
