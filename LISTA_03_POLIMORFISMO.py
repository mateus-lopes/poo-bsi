#1
class Animal:
    def falar(self):
        raise NotImplementedError("subclasses devem implementar este método")

class Cachorro(Animal):
    def falar(self):
        return "au au"

class Gato(Animal):
    def falar(self):
        return "miau"

class Peixe(Animal):
    def falar(self):
        return "blub blub"

animais = [Cachorro(), Gato(), Peixe()]
for animal in animais:
    print(animal.falar())

#2
class Animal:
    def falar(self):
        raise NotImplementedError("subclasses devem implementar este método")

class Cachorro(Animal):
    def falar(self):
        return "au au"

class Gato(Animal):
    def falar(self):
        return "miau"

animais = [Cachorro(), Gato()]
for animal in animais:
    print(animal.falar())

#3
class Carro:
    def dirigir(self):
        raise NotImplementedError("subclasses devem implementar este método")

class CarroGasolina(Carro):
    def dirigir(self):
        return "dirigindo carro a gasolina"

class CarroEletrico(Carro):
    def dirigir(self):
        return "dirigindo carro elétrico"

def demonstrar_direcao(carro: Carro):
    print(carro.dirigir())

carros = [CarroGasolina(), CarroEletrico()]
for carro in carros:
    demonstrar_direcao(carro)

#4
import math

class Forma:
    def area(self):
        raise NotImplementedError("subclasses devem implementar este método")

class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio

    def area(self):
        return math.pi * (self.raio ** 2)

class Quadrado(Forma):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado ** 2

formas = [Circulo(5), Quadrado(4)]
for forma in formas:
    print(forma.area())


#5
class Empregado:
    def pagar_salario(self):
        raise NotImplementedError("subclasses devem implementar este método")

class EmpregadoHora(Empregado):
    def __init__(self, horas_trabalhadas, valor_hora):
        self.horas_trabalhadas = horas_trabalhadas
        self.valor_hora = valor_hora

    def pagar_salario(self):
        return self.horas_trabalhadas * self.valor_hora

class EmpregadoMes(Empregado):
    def __init__(self, salario_mensal):
        self.salario_mensal = salario_mensal

    def pagar_salario(self):
        return self.salario_mensal

empregados = [EmpregadoHora(160, 20), EmpregadoMes(3000)]
for empregado in empregados:
    print(empregado.pagar_salario())

#6
class ContaBancaria:
    def __init__(self, saldo=0):
        self.saldo = saldo

    def deposito(self, valor):
        self.saldo += valor
        return self.saldo

    def retirada(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
        else:
            print("saldo insuficiente")
        return self.saldo

class ContaPoupanca(ContaBancaria):
    taxa_juros = 0.05

    def adicionar_juros(self):
        self.saldo += self.saldo * self.taxa_juros
        return self.saldo

class ContaCorrente(ContaBancaria):
    taxa_juros = 0.01

    def adicionar_juros(self):
        self.saldo += self.saldo * self.taxa_juros
        return self.saldo

conta_poupanca = ContaPoupanca(1000)
conta_corrente = ContaCorrente(1000)
conta_poupanca.deposito(500)
conta_corrente.retirada(200)
conta_poupanca.adicionar_juros()
conta_corrente.adicionar_juros()
print("saldo conta poupança:", conta_poupanca.saldo)
print("saldo conta corrente:", conta_corrente.saldo)
