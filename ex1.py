'''

1) (a) Uma coleção de variáveis e funções trabalhando com essas variáveis.

2) (a) Um objeto nos dá a capacidade de trabalhar com a classe e ter várias instâncias desta mesma classe.

3) (b) Uma variável dentro de uma classe.

4) (a) Uma função dentro de uma classe.

5)  Nome da classe: Usuario
    Propriedades: primeiro_nome, sobrenome
    Método: dizer_ola()

'''

# 6)
class Usuario:
    def __init__(self, primeiro_nome, sobrenome):
        self.primeiro_nome = primeiro_nome
        self.sobrenome = sobrenome

    def dizer_ola(self):
        return f'\nOlá, {self.primeiro_nome} {self.sobrenome}.'

# 7)
usuario1 = Usuario('','')

# 8)
usuario1.primeiro_nome = 'Mateus'
usuario1.sobrenome = 'Lopes'

# 9)
print('Nome do usuário:', usuario1.primeiro_nome)
print('Sobrenome do usuário:', usuario1.sobrenome)

# 10)
print(usuario1.dizer_ola())

# 11) 
usuario2 = Usuario('Jane', 'Silva')
print(usuario2.dizer_ola())