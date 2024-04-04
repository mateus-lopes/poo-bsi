"""
    -----------------------------------------------------
    Modificador	Classe Mãe	Classe Filha	Escopo Global
    -----------------------------------------------------
    public	    Sim	        Sim	            Sim
    protected	Sim	        Sim	            Não
    private	    Sim	        Não	            Não
    -----------------------------------------------------

    8) Resposta: A classe Admin não consegue acessar o atributo __nomeUsuario da classe Usuario, pois o atributo é privado.
"""

class Usuario:
    def __init__(self):
        self.__nomeUsuario = None

    def set_nomeUsuario(self, nome):
        self.__nomeUsuario = nome

    def get_nomeUsuario(self):
        return self.__nomeUsuario

class Admin(Usuario):
    def __init__(self):
        super().__init__()

    def escrevaNome(self):
        return "Admin"

    def digaOla(self):
        return f"Olá Admin, {self.get_nomeUsuario()}"

admin1 = Admin()
admin1.set_nomeUsuario("Baltazar")
print(admin1.digaOla())
