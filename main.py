
class Locadora:
    def __init__(self,codigo,nome,valor_locacao,prazo_locacao,catalogo):
        self._codigo = codigo
        self._nome = nome.title()
        self._valor_locacao = valor_locacao
        self._prazo_locacao = prazo_locacao
        self._catalogo = catalogo #lista de filmes

    def __getitem__(self,item):
        return self._catalogo[item]

    def __len__(self):
        return len(self._catalogo)

    @property
    def nome(self):
        return self._nome

    def consulta_filme_catalogo(self,filme):
        if(filme in self._catalogo):
            print(f"A locadora {self._nome} possui o filme {filme.nome}!")
        else:
            print(f"A locadora {self._nome} não possui o filme {filme.nome}!")


class Filmes:
    def __init__(self, codigo, nome, ano, genero, numero_copias,):
        self._codigo = codigo
        self._nome = nome.title()
        self.ano = ano
        self.genero = genero
        self._numero_copias = numero_copias

    @property
    def nome(self):
        return self._nome
    @property
    def numero_copias(self):
        return self._numero_copias

class Clientes:
    def __init__(self,id):
        self.id = id

class Locacao:
    def __init__(self,id_cliente,id_filme,id_locadora):
        self.id_cliente = id_cliente
        self.id_filme = id_filme
        self.id_locadora = id_locadora


toy_story = Filmes(1,"toy story",2010,"animação",2)
vingadores = Filmes(2,"vingadores",2018,"aventura",5)
homem_de_ferro = Filmes(3,"homem de ferro",2010,"aventura",1)
moana = Filmes(4,"moana",2010,"animação",10)
jumanji = Filmes(5,"jumanji",2017,"ação",5)

catalogo_newloc = [toy_story,vingadores,homem_de_ferro,moana]
catalogo_era = [toy_story,vingadores,homem_de_ferro,moana,jumanji]
catalogo_londrina = [toy_story,moana,jumanji]

newloc = Locadora(1010,"new loc",15,14,catalogo_newloc)
era = Locadora(1020,"era",12,7,catalogo_era)
londrina = Locadora(2043,"londrina",10,6,catalogo_londrina)

locacao1 = Locacao(1,4,1010)
locacao2 = Locacao(1,5,1020)

lista_locacao= [locacao1,locacao2]

while(True):
    print(f'Menu Locadora:\n'
          f'1 - Cadastrar Locadora\n'
          f'2 - Cadastrar Filme\n'
          f'3 - Cadastrar Cliente\n'
          f'4 - Alugar Filme')
    escolha = input('Escolha a opção: ')

    if (escolha == '1'):
        print('Em construção')
    elif (escolha == '2'):
        print('Em construção')
    elif (escolha == '3'):
        print('Em construção')
    elif (escolha == '4'):
        id_cliente = input('Codigo Cliente: ')
        id_filme = input('Codigo Filme: ')
        id_locadora = input('Codigo Locadora: ')

        locacao3 = Locacao(id_cliente,id_filme,id_locadora)
        lista_locacao.append(locacao3)

        print('Locação realizada com sucesso!')

# for locacao in lista_locacao:
#     print(f'id cliente: {locacao.id_cliente}, id filme: {locacao.id_filme} e id locadora {locacao.id_locadora}')

# print(f'A locadora {newloc.nome} possui um catálogo com {len(newloc)} filmes!')
# print(f'Segue a lista de filmes da locadora {newloc.nome}:')
# for filme in newloc:
#     print(f'O filme {filme._nome} possui {filme.numero_copias} exemplares disponíveis!')
#
# print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
#
#
# print(f'A locadora {era.nome} possui um catálogo com {len(era)} filmes!')
# print(f'Segue a lista de filmes da locadora {era.nome}:')
# for filme in era:
#     print(f'O filme {filme._nome} possui {filme.numero_copias} exemplares disponíveis!')
#
# print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
#
# print(f'A locadora {londrina.nome} possui um catálogo com {len(londrina)} filmes!')
# print(f'Segue a lista de filmes da locadora {londrina.nome}:')
# for filme in londrina:
#     print(f'O filme {filme._nome} possui {filme.numero_copias} exemplares disponíveis!')
#
# print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
#
# newloc.consulta_filme_catalogo(vingadores)