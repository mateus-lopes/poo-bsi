from random import randint

print("\n-- CLASSE BOLA --\n")
class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def trocaCor(self, nova_cor):
        self.cor = nova_cor

    def mostraCor(self):
        return self.cor
    
# atributos = input("Informe a cor, circunferência e material da bola (separados por um espaço): ").split(' ')
# bola1 = Bola(atributos[0], atributos[1], atributos[2])
bola1 = Bola("Roxo", 25, "Borracha")
print("Cor da bola:", bola1.mostraCor())
bola1.trocaCor("Marrom")
print("Nova cor da bola:", bola1.mostraCor())

print("\n-- CLASSE QUADRADO --\n")
class Quadrado:
    def __init__(self, lado):
        self.lado = lado

    def mudarValorLado(self, novo_lado):
        self.lado = novo_lado

    def retornarValorLado(self):
        return self.lado

    def calcularArea(self):
        return self.lado ** 2
    
# lado_quadrado = float(input("Informe o lado do quadrado: "))
# quadrado1 = Quadrado(lado_quadrado)
quadrado1 = Quadrado(16)
print("Lado do quadrado:", quadrado1.retornarValorLado())
quadrado1.mudarValorLado(5)
print("Novo lado do quadrado:", quadrado1.retornarValorLado())
print("Área do quadrado:", quadrado1.calcularArea())

print("\n-- CLASSE RETÂNGULO --\n")
class Retangulo:
    def __init__(self, ladoA, ladoB):
        self.ladoA = ladoA
        self.ladoB = ladoB

    def mudarValorLados(self, novo_ladoA, novo_ladoB):
        self.ladoA = novo_ladoA
        self.ladoB = novo_ladoB

    def retornarValorLados(self):
        return self.ladoA, self.ladoB

    def calcularArea(self):
        return self.ladoA * self.ladoB

    def calcularPerimetro(self):
        return 2 * (self.ladoA + self.ladoB)
    
# c. Crie um programa que utilize esta classe.
comprimento = float(input("Informe o comprimento do local (em metros): "))
largura = float(input("Informe a largura do local (em metros): "))
local = Retangulo(comprimento, largura)
comprimento_piso = float(input("Informe o comprimento do piso (em metros): "))
largura_piso = float(input("Informe a largura do piso (em metros): "))
area_piso = comprimento_piso * largura_piso
quantidade_pisos = local.calcularArea() / area_piso
print(f"Quantidade de pisos necessários: {quantidade_pisos}")
comprimento_rodape = float(input("Informe o comprimento do rodapé (em metros): "))
quantidade_rodapes = local.calcularPerimetro() / comprimento_rodape
print(f"Quantidade de rodapés necessários: {quantidade_rodapes}")

print("\n-- CLASSE PESSOA --\n")
class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self):
        self.idade = self.idade + 1
        if self.idade < 21:
            self.altura = self.idade + 0.5

    def engordar(self, peso):
        self.peso += peso

    def emagrecer(self, peso):
        self.peso -= peso

    def crescer(self, altura):
        self.altura += altura

# atributos_pessoa = input("Informe o nome, idade, peso e altura da pessoa (separados por um espaço): ").split(' ')
# pessoa1 = Pessoa(atributos_pessoa[0], int(atributos_pessoa[1]), int(atributos_pessoa[2]), int(atributos_pessoa[3]))
pessoa1 = Pessoa("Fulano", 20, 64, 1.78)
print("Altura da pessoa:", pessoa1.altura)
pessoa1.envelhecer()
print("Nova idade da pessoa:", pessoa1.idade)
print("Nova altura da pessoa:", pessoa1.altura)
pessoa1.engordar(5)
print("Novo peso da pessoa:", pessoa1.peso)
pessoa1.emagrecer(5)
print("Novo peso da pessoa:", pessoa1.peso)
pessoa1.crescer(0.05)
print("Nova altura da pessoa:", pessoa1.altura)

print("\n-- CLASSE CONTA CORRENTE --\n")
class ContaCorrente:
    def __init__(self, numero_conta, nome_correntista, saldo=0):
        self.numero_conta = numero_conta
        self.nome_correntista = nome_correntista
        self.saldo = saldo

    def alterarNome(self, novo_nome):
        self.nome_correntista = novo_nome

    def deposito(self, valor):
        self.saldo += valor

    def saque(self, valor):
        self.saldo -= valor

# atributos_conta = input("Informe o número da conta e o nome do correntista (separados por um espaço): ").split(' ')
# conta1 = ContaCorrente(atributos_conta[0], atributos_conta[1])
conta1 = ContaCorrente("55342-6", "Fulano")
print("Saldo da conta:", conta1.saldo)
conta1.deposito(1500)
print("Novo saldo da conta:", conta1.saldo)
conta1.saque(900)
print("Novo saldo da conta:", conta1.saldo)

print("\n-- CLASSE TV --\n")
class TV:
    def __init__(self, canal=1, volume=10):
        self.canal = canal
        self.volume = volume

    def mudarCanal(self, novo_canal):
        if 1 <= novo_canal <= 100:
            self.canal = novo_canal

    def aumentarVolume(self):
        if self.volume < 100:
            self.volume += 1

    def diminuirVolume(self):
        if self.volume > 0:
            self.volume -= 1

tv1 = TV()
print("Canal da TV:", tv1.canal)
print("Volume da TV:", tv1.volume)
tv1.mudarCanal(12)
print("Novo canal da TV:", tv1.canal)
tv1.aumentarVolume()
print("Novo volume da TV:", tv1.volume)
tv1.diminuirVolume()
print("Novo volume da TV:", tv1.volume)

print("\n-- CLASSE BICHINHO VIRTUAL --\n")
class BichinhoVirtual:
    def __init__(self, nome, fome, saude, idade):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade

    def alterarNome(self, novo_nome):
        self.nome = novo_nome

    def alterarFome(self, nova_fome):
        self.fome = nova_fome

    def alterarSaude(self, nova_saude):
        self.saude = nova_saude

    def alterarIdade(self, nova_idade):
        self.idade = nova_idade

    def retornarNome(self):
        return self.nome

    def retornarFome(self):
        return self.fome

    def retornarSaude(self):
        return self.saude

    def retornarIdade(self):
        return self.idade

    def retornarHumor(self):
        return self.saude - self.fome
    
# atributos_bichinho = input("Informe o nome, fome, saúde e idade do bichinho (separados por um espaço): ").split(' ')
# bichinho1 = BichinhoVirtual(atributos_bichinho[0], int(atributos_bichinho[1]), int(atributos_bichinho[2]), int(atributos_bichinho[3]))
bichinho1 = BichinhoVirtual("Billy", 50, 50, 5)
print("Nome do bichinho:", bichinho1.retornarNome())
print("Fome do bichinho:", bichinho1.retornarFome())
print("Saúde do bichinho:", bichinho1.retornarSaude())
print("Idade do bichinho:", bichinho1.retornarIdade())
print("Humor do bichinho:", bichinho1.retornarHumor())
bichinho1.alterarNome("Juninho")
bichinho1.alterarFome(40)
bichinho1.alterarSaude(100)
bichinho1.alterarIdade(9)
print("Nome do bichinho:", bichinho1.retornarNome())
print("Fome do bichinho:", bichinho1.retornarFome())
print("Saúde do bichinho:", bichinho1.retornarSaude())
print("Idade do bichinho:", bichinho1.retornarIdade())
print("Humor do bichinho:", bichinho1.retornarHumor())

print("\n-- CLASSE MACACO --\n")
class Macaco:
    def __init__(self, nome):
        self.nome = nome
        self.bucho = []

    def comer(self, alimento):
        self.bucho.append(alimento)

    def verBucho(self):
        return self.bucho

    def digerir(self):
        self.bucho = []

atributos_macaco = input("Informe o nome dos dois macacos (separados por um espaço): ").split(' ')
macaco1 = Macaco(atributos_macaco[0])
macaco2 = Macaco(atributos_macaco[1])
macaco1.comer("Banana")
macaco1.comer("Maçã")
macaco1.comer("Pera")
print(f"Bucho do macaco {atributos_macaco[0]}:", macaco1.verBucho())
macaco1.digerir()
print(f"Bucho do macaco {atributos_macaco[0]}:", macaco1.verBucho())
macaco2.comer("Banana")
macaco2.comer("Maçã")
macaco2.comer("Pera")
print(f"Bucho do macaco {atributos_macaco[1]}:", macaco2.verBucho())
macaco1.comer(macaco2)
print(f"Bucho do macaco {atributos_macaco[0]}:", macaco1.verBucho())
macaco1.digerir()
print(f"Bucho do macaco {atributos_macaco[0]}:", macaco1.verBucho())

print("\n-- CLASSE PONTO_RETANGULO --\n")
class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def imprimir(self):
        print(f"({self.x}, {self.y})")

class Ponto_Retangulo:
    def __init__(self, largura, altura, ponto):
        self.largura = largura
        self.altura = altura
        self.ponto = ponto

    def centro(self):
        centro_x = self.ponto.x + self.largura / 2
        centro_y = self.ponto.y + self.altura / 2
        return Ponto(centro_x, centro_y)
    
def obterValoresInteiros(mensagem):
    while True:
        try:
            valores = list(map(int, input(mensagem).split()))
            if len(valores) != 2:
                raise ValueError("Informe exatamente dois valores separados por um espaço.")
            return valores
        except ValueError as e:
            print(f"Erro: {e}. Por favor, insira novamente.")

atributos_ponto = obterValoresInteiros("Informe as coordenadas do ponto (separadas por um espaço): ")
atributos_retangulo = obterValoresInteiros("Informe a largura e a altura do retângulo (separadas por um espaço): ")
ponto1 = Ponto(atributos_ponto[0], atributos_ponto[1])
retangulo1 = Ponto_Retangulo(atributos_retangulo[0], atributos_retangulo[1], ponto1)
while True:
    print("Opções:")
    print("1 - Alterar largura")
    print("2 - Alterar altura")
    print("3 - Imprimir centro")
    print("0 - Sair")

    opcao = int(input("Digite a opção: "))

    if opcao == 1:
        nova_largura = int(input("Digite a nova largura: "))
        retangulo1.largura = nova_largura
    elif opcao == 2:
        nova_altura = int(input("Digite a nova altura: "))
        retangulo1.altura = nova_altura
    elif opcao == 3:
        centro_retangulo1 = retangulo1.centro()
        centro_retangulo1.imprimir()
    elif opcao == 0:
        break
    else:
        print("Opção inválida!")

print("\n-- CLASSE BOMBA DE COMBUSTÍVEL --\n")
class BombaCombustivel: 
    def __init__(self, tipoCombustivel, valorLitro, quantidadeCombustivel):
        self.tipoCombustivel = tipoCombustivel
        self.valorLitro = valorLitro
        self.quantidadeCombustivel = quantidadeCombustivel

    def abastecerPorValor(self, valor):
        litros = valor / self.valorLitro
        self.quantidadeCombustivel -= litros
        return litros

    def abastecerPorLitro(self, litros):
        valor = litros * self.valorLitro
        self.quantidadeCombustivel -= litros
        return valor

    def alterarValor(self, novoValor):
        self.valorLitro = novoValor

    def alterarCombustivel(self, novoCombustivel):
        self.tipoCombustivel = novoCombustivel

    def alterarQuantidadeCombustivel(self, nova_quantidade):
        self.quantidadeCombustivel = nova_quantidade

# atributos_bomba = input("Informe o tipo de combustível, valor do litro e quantidade de combustível da bomba (separados por um espaço): ").split(' ')
# bomba1 = BombaCombustivel(atributos_bomba[0], int(atributos_bomba[1]), int(atributos_bomba[2]))
bomba1 = BombaCombustivel("Gasolina", 5, 1000)
print("Quantidade de litros abastecidos:", bomba1.abastecerPorValor(50))
print("Quantidade de litros abastecidos:", bomba1.abastecerPorLitro(10))
bomba1.alterarValor(4)
bomba1.alterarCombustivel("Etanol")
bomba1.alterarQuantidadeCombustivel(500)

print("\n-- CLASSE CARRO --\n")
class Carro:
    def __init__(self, consumo):
        self.consumo = consumo
        self.combustivel = 0

    def andar(self, distancia):
        self.combustivel -= distancia / self.consumo

    def obterGasolina(self):
        return self.combustivel

    def adicionarGasolina(self, litros):
        self.combustivel += litros

meuFusca = Carro(15)
meuFusca.adicionarGasolina(20)
meuFusca.andar(100)
print("Combustível restante no tanque:", meuFusca.obterGasolina())

print("\n-- CLASSE CONTA DE INVESTIMENTO --\n")
class ContaInvestimento:
    def __init__(self, saldo_inicial, taxa_juros):
        self.saldo = saldo_inicial
        self.taxa_juros = taxa_juros

    def adicioneJuros(self):
        self.saldo += self.saldo * (self.taxa_juros / 100)

conta1 = ContaInvestimento(1000, 10)
for _ in range(5):
    conta1.adicioneJuros()
print("Saldo da conta de investimento:", conta1.saldo)

print("\n-- CLASSE FUNCIONÁRIO --\n")
class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def aumentarSalario(self, porcentual_aumento):
        self.salario += self.salario * (porcentual_aumento / 100)

funcionario1 = Funcionario("Fulano", 1000)
print("Salário do funcionário:", funcionario1.salario)
funcionario1.aumentarSalario(10)
print("Novo salário do funcionário:", funcionario1.salario)


print("\n-- CLASSE BICHINHO VIRTUAL++ --\n")
class BichinhoVirtualMelhorado:
    def __init__(self, nome, fome, saude, idade):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade

    def __str__(self):
        return f"Nome: {self.nome}, Fome: {self.fome}, Saúde: {self.saude}, Idade: {self.idade}"

    def alimentar(self, alimento, tempo):
        if (self.fome - alimento) <= 0 or (self.fome == 0):
            self.fome = 0
        else:
            self.fome -= alimento

        if self.saude >= 100:
            self.saude = 100
        else:
            self.saude += tempo / 2

    def brincar(self, tempo):
        if self.fome > 100:
            self.fome = 100
        else:
            self.fome += tempo

        if self.saude >= 100:
            self.saude = 100
        else:
            self.saude += tempo / 2

    def retornarNome(self):
        return self.nome

    def retornarFome(self):
        return self.fome

    def retornarSaude(self):
        return self.saude

    def retornarIdade(self):
        return self.idade
    
    def retornarHumor(self):
        return self.saude - self.fome
    
# atributos_bichinho = input("Informe o nome, fome, saúde e idade do bichinho (separados por um espaço): ").split(' ')
# bichinho1 = BichinhoVirtualMelhorado(atributos_bichinho[0], int(atributos_bichinho[1]), int(atributos_bichinho[2]), int(atributos_bichinho[3]))
bichinho1 = BichinhoVirtualMelhorado("Bichinho", 25, 50, 9)
while True:
    print("Opções:")
    print("1 - Alimentar")
    print("2 - Brincar")
    print("3 - Ver humor")
    print("4 - Porta escondida")
    print("0 - Sair")

    opcao = int(input("Digite a opção: "))

    if opcao == 1:
        alimento = int(input("Digite a quantidade de alimento: "))
        tempo = int(input("Digite o tempo de alimentação: "))
        bichinho1.alimentar(alimento, tempo)
    elif opcao == 2:
        tempo = int(input("Digite o tempo de brincadeira: "))
        bichinho1.brincar(tempo)
    elif opcao == 3:
        print("Humor do bichinho:", bichinho1.retornarHumor())
    elif opcao == 4:
        print(bichinho1)
    elif opcao == 0:
        break
    else:
        print("Opção inválida!")

print("\n-- CLASSE FAZENDA DE BICHINHOS --\n")
class FazendaBichinhos:
    def __init__(self, quantidade_bichinhos):
        self.bichinhos = []
        for _ in range(quantidade_bichinhos):
            self.bichinhos.append(BichinhoVirtualMelhorado("Bichinho", randint(0, 100), randint(0, 100), randint(0, 14)))

    def alimentar(self, alimento, tempo):
        for bichinho in self.bichinhos:
            bichinho.alimentar(alimento, tempo)

    def brincar(self, tempo):
        for bichinho in self.bichinhos:
            bichinho.brincar(tempo)

    def verHumor(self):
        for bichinho in self.bichinhos:
            print(f"Humor do bichinho {bichinho.retornarNome()}: {bichinho.retornarHumor()}")

quantidade_bichinhos = int(input("Informe a quantidade de bichinhos na fazenda: "))
fazenda1 = FazendaBichinhos(quantidade_bichinhos)
while True:
    print("Opções:")
    print("1 - Alimentar")
    print("2 - Brincar")
    print("3 - Ver humor")
    print("0 - Sair")

    opcao = int(input("Digite a opção: "))

    if opcao == 1:
        alimento = int(input("Digite a quantidade de alimento: "))
        tempo = int(input("Digite o tempo de alimentação: "))
        fazenda1.alimentar(alimento, tempo)
    elif opcao == 2:
        tempo = int(input("Digite o tempo de brincadeira: "))
        fazenda1.brincar(tempo)
    elif opcao == 3:
        fazenda1.verHumor()
    elif opcao == 0:
        break
    else:
        print("Opção inválida!")

