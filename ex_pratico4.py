# 1) ( D )

# 2) 

class Usuario:
    def __init__(self):
        self.__primeiro_nome = ""

    @property
    def primeiro_nome(self):
        return self.__primeiro_nome

    def set_primeiro_nome(self, param):
        self.__primeiro_nome = param

    def get_primeiro_nome(self):
        return self.__primeiro_nome

usuario1 = Usuario()
usuario1.set_primeiro_nome("Joe")

print("Primeiro nome do usuário é  ", usuario1.get_primeiro_nome())

# 3)
class Empregado:
    def __init__(self, nome, salario, projeto):
        self.nome = nome
        self.__salario = salario 
        self.projeto = projeto

    def trabalho(self):
        print(f"{self.nome} está trabalhando com o projeto {self.projeto}")

    def mostrar(self):
        print(f"Detalhes: \nNome: {self.nome}\nSalário: {self.__salario}")

empregado1 = Empregado("Mateus", 2200, "Mapa Estratégico")
empregado1.trabalho()
empregado1.mostrar()

# 4)
class Robo:
    def __init__(self, nome, ano_construcao):
        self.__nome = nome 
        self.__ano_construcao = ano_construcao 

    def diga_alo(self):
        print(f"{self.__nome} foi construído no ano {self.__ano_construcao}")

    def get_nome(self):
        return self.__nome

    def set_nome(self, param):
        self.__nome = param

    def get_ano_construcao(self):
        return self.__ano_construcao

    def set_ano_construcao(self, param):
        self.__ano_construcao = param

robo1 = Robo("ROBOTO", 2004)
robo1.diga_alo()
robo1.set_nome("ROBOTINHO")
robo1.set_ano_construcao(2008)

print("Novo nome:", robo1.get_nome())
print("Novo ano de construção:", robo1.get_ano_construcao())


class Laptop:
    def __init__(self):
        self.__preco = None

    def get_preco(self):
        return self.__preco

    def set_preco(self, param):
        self.__preco = param

laptop1 = Laptop()
print("Preço do laptop:", laptop1.get_preco())

laptop1.set_preco(7699.99)
print("Novo preço do laptop:", laptop1.get_preco())


class Pessoa:
    def __init__(self):
        self.__primeiroNome = ""
        self.__ultimoNome = ""

    def getPrimeiroNome(self):
        return self.__primeiroNome

    def setPrimeiroNome(self, param):
        self.__primeiroNome = param

    def getUltimoNome(self):
        return self.__ultimoNome

    def setUltimoNome(self, param):
        self.__ultimoNome = param

pessoa1 = Pessoa()
pessoa1.setPrimeiroNome("João")
pessoa1.setUltimoNome("Carvalho")
print("Primeiro nome:", pessoa1.getPrimeiroNome())
print("Último nome:", pessoa1.getUltimoNome())
