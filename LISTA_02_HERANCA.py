class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def imprimir_informacoes(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")


class Aluno(Pessoa):
    def __init__(self, nome, idade, nota):
        super().__init__(nome, idade)
        self.nota = nota
    
    def imprimir_informacoes(self):
        super().imprimir_informacoes()
        print(f"Nota: {self.nota}")


class Veiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    
    def imprimir_informacoes(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Ano: {self.ano}")


class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, quantidade_de_portas):
        super().__init__(marca, modelo, ano)
        self.quantidade_de_portas = quantidade_de_portas
    
    def imprimir_informacoes(self):
        super().imprimir_informacoes()
        print(f"Quantidade de portas: {self.quantidade_de_portas}")


class Moto(Veiculo):
    def __init__(self, marca, modelo, ano, cilindradas):
        super().__init__(marca, modelo, ano)
        self.cilindradas = cilindradas
    
    def imprimir_informacoes(self):
        super().imprimir_informacoes()
        print(f"Cilindradas: {self.cilindradas}")


class Animal:
    def __init__(self, nome, peso):
        self.nome = nome
        self.peso = peso
    
    def comer(self):
        print(f"{self.nome} está comendo.")


class Cachorro(Animal):
    def latir(self):
        print("Au au!")


class Gato(Animal):
    def miar(self):
        print("Miau!")


class Funcionario(Pessoa):
    def __init__(self, nome, idade, salario):
        super().__init__(nome, idade)
        self.salario = salario
    
    def aumento(self, porcentagem):
        self.salario += self.salario * (porcentagem / 100)


class Forma:
    def area(self):
        pass


class Retangulo(Forma):
    def __init__(self, comprimento, largura):
        self.comprimento = comprimento
        self.largura = largura
    
    def area(self):
        return self.comprimento * self.largura


class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio
    
    def area(self):
        return 3.14 * self.raio ** 2
    

class Conta():
    def __init__(self, numero, saldo, cliente):
        self.numero = numero
        self.saldo = saldo
        self.cliente = cliente

    def creditar(self, valor):
        if valor > 0:
            self.saldo += valor
        else:
            print("Valor inválido para crédito.")

    def debitar(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
        else:
            print("Saldo insuficiente ou valor inválido para débito.")

class CCorrente(Conta):
    def getSaldo(self):
        return self.saldo

class CEspecial(Conta):
    def __init__(self, numero, saldo, cliente, limite):
        super().__init__(numero, saldo, cliente)
        self.limite = limite

    def getSaldo(self):
        return self.saldo + self.limite

class CPoupanca(Conta):
    def __init__(self, numero, saldo, cliente, saldoMinimo):
        super().__init__(numero, saldo, cliente)
        self.saldoMinimo = saldoMinimo

    def debitar(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
        elif valor <= self.saldoMinimo:
            print("Saldo mínimo insuficiente.")
        else:
            print("Saldo insuficiente ou valor inválido para débito.")

    def getSaldo(self):
        return self.saldo

class CInvestimento(Conta):
    def __init__(self, numero, saldo, cliente, dataInvestimento, periodo):
        super().__init__(numero, saldo, cliente)
        self.dataInvestimento = dataInvestimento
        self.periodo = periodo

    def atualizarSaldo(self):
        pass

    def getSaldo(self):
        return self.saldo + self.atualizarSaldo()

class Empregado:
    def __init__(self, codigo, nome, email, salario):
        self.codigo = codigo
        self.nome = nome
        self.email = email
        self.salario = salario

    def getSalario(self):
        return self.salario

    def aumentoSalario(self, percentual):
        self.salario += self.salario * (percentual / 100)
        return self.salario

class Chefe(Empregado):
    def __init__(self, codigo, nome, email, salario, beneficio):
        super().__init__(codigo, nome, email, salario)
        self.beneficio = beneficio

    def aumentoSalario(self, percentual):
        self.salario += self.salario * (percentual / 100) + self.beneficio
        return self.salario

class Estagiario(Empregado):
    def __init__(self, codigo, nome, email, salario, desconto):
        super().__init__(codigo, nome, email, salario)
        self.desconto = desconto

    def aumentoSalario(self, percentual):
        self.salario += self.salario * (percentual / 100) - self.desconto
        return self.salario
    
class Ingresso:
    def __init__(self, valor):
        self.valor = valor
    
    def imprimeValor(self):
        print(f"Valor do ingresso: R${self.valor:.2f}")

class VIP(Ingresso):
    def __init__(self, valor, adicional):
        super().__init__(valor)
        self.adicional = adicional
    
    def valorIngressoVIP(self):
        return self.valor + self.adicional

class Normal(Ingresso):
    def imprimeValor(self):
        print("Ingresso Normal")

class CamaroteInferior(VIP):
    def __init__(self, valor, adicional, localizacao):
        super().__init__(valor, adicional)
        self.localizacao = localizacao
    
    def getLocalizacao(self):
        return self.localizacao
    
    def imprimeLocalizacao(self):
        print(f"Localização do ingresso: {self.localizacao}")

class CamaroteSuperior(VIP):
    def __init__(self, valor, adicional):
        super().__init__(valor, adicional)
    
    def valorIngresso(self):
        return self.valorIngressoVIP()

class Funcionario:
    def __init__(self, nome, endereco, telefone, email):
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone
        self.email = email
    
    def exibeDados(self):
        print(f"Nome: {self.nome}")
        print(f"Endereço: {self.endereco}")
        print(f"Telefone: {self.telefone}")
        print(f"Email: {self.email}")

class Assistente(Funcionario):
    def __init__(self, nome, endereco, telefone, email, matricula):
        super().__init__(nome, endereco, telefone, email)
        self.matricula = matricula
    
    def getMatricula(self):
        return self.matricula

class Tecnico(Assistente):
    def __init__(self, nome, endereco, telefone, email, matricula, bonus):
        super().__init__(nome, endereco, telefone, email, matricula)
        self.bonus = bonus
    
    def exibeDados(self):
        super().exibeDados()
        print(f"Matrícula: {self.matricula}")
        print(f"Bônus salarial: R${self.bonus:.2f}")

class Administrativo(Assistente):
    def __init__(self, nome, endereco, telefone, email, matricula, turno, adicional_noturno):
        super().__init__(nome, endereco, telefone, email, matricula)
        self.turno = turno
        self.adicional_noturno = adicional_noturno
    
    def exibeDados(self):
        super().exibeDados()
        print(f"Matrícula: {self.matricula}")
        print(f"Turno: {self.turno}")
        print(f"Adicional noturno: R${self.adicional_noturno:.2f}")

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

class Rica(Pessoa):
    def __init__(self, nome, idade, dinheiro):
        super().__init__(nome, idade)
        self.dinheiro = dinheiro

    def fazCompras(self):
        print(f"{self.nome} está fazendo compras.")

class Pobre(Pessoa):
    def trabalha(self):
        print(f"{self.nome} está trabalhando.")

class Miseravel(Pessoa):
    def mendiga(self):
        print(f"{self.nome} está mendigando.")

# TESTES COM AS CLASSES

# veiculo
carro1 = Carro("Volkswagen", "Gol", 2020, 4)
carro1.imprimir_informacoes()
moto1 = Moto("Honda", "CG 160", 2021, "160cc")
moto1.imprimir_informacoes()

# animal
cachorro1 = Cachorro("Totó", 15)
cachorro1.latir()
gato1 = Gato("Mingau", 5)
gato1.miar()

# funcionarios / empregados
funcionario1 = Funcionario("Carlos", 40, 3000)
funcionario1.aumento(10)
assistente1 = Assistente("Joana", "Rua A", "12345678", "joana@email.com", "123")
print(assistente1.getMatricula())
tecnico1 = Tecnico("Carlos", "Rua B", "87654321", "carlos@email.com", "456", 200)
tecnico1.exibeDados()
administrativo1 = Administrativo("Julia", "Rua C", "11223344", "julia@email.com", "789", "Noite", 300)
administrativo1.exibeDados()
empregado1 = Empregado("001", "Roberto", "roberto@email.com", 2500)
print(empregado1.getSalario())
chefe1 = Chefe("002", "Fernanda", "fernanda@email.com", 5000, 1000)
print(chefe1.aumentoSalario(10))
estagiario1 = Estagiario("003", "Lucas", "lucas@email.com", 1000, 100)
print(estagiario1.aumentoSalario(10))

# formas
retangulo1 = Retangulo(10, 5)
print(retangulo1.area())
circulo1 = Circulo(5)
print(circulo1.area())

# contas
ccorrente1 = CCorrente("1234", 1000, "José")
print(ccorrente1.getSaldo())
cespecial1 = CEspecial("5678", 2000, "Ana", 500)
print(cespecial1.getSaldo())
cpoupanca1 = CPoupanca("9012", 1500, "Pedro", 300)
cpoupanca1.debitar(100)
print(cpoupanca1.getSaldo())

# ingressos
ingresso1 = Ingresso(50)
ingresso1.imprimeValor()
vip1 = VIP(50, 20)
print(vip1.valorIngressoVIP())
camaroteInferior1 = CamaroteInferior(50, 20, "Setor Sul")
camaroteInferior1.imprimeLocalizacao()

# pessoas
aluno1 = Aluno("Maria", 20, 9.5)
aluno1.imprimir_informacoes()
rica1 = Rica("Eduardo", 45, 100000)
rica1.fazCompras()
pobre1 = Pobre("Marcos", 30)
pobre1.trabalha()
miseravel1 = Miseravel("Cláudio", 25)
miseravel1.mendiga()