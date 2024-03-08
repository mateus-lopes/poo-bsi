class Usuario:
    def __init__(self, primeiro_nome, sobrenome):
        self.primeiro_nome = primeiro_nome
        self.sobrenome = sobrenome

    def getNomeCompleto(self):
        return f"{self.primeiro_nome} {self.sobrenome}"

usuario1 = Usuario("Professor", "PC")

print("Nome completo deste usuário é ", usuario1.getNomeCompleto())