"""

1) C 

"""

class Usuario:
    def __init__(self, primeiro_nome, sobrenome):
        self.primeiro_nome = primeiro_nome
        self.sobrenome = sobrenome
        self.nome_completo = f'{primeiro_nome} {sobrenome}'

    def dizer_ola(self):
        return f'\nOlá, {self.nome_completo}.'


usuario1 = Usuario('Mateus', 'Lopes Albano')
usuario2 = Usuario('Jane', 'Silva')

print(usuario1.dizer_ola())
print(usuario2.dizer_ola())