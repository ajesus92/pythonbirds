class Pessoa:
    def __init__(self, nome=None, idade=35):
        self.nome = nome
        self.idade = idade

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    p = Pessoa('Renzo', 33)
    print(p.cumprimentar())
    print(p.nome)
    print(p.idade)