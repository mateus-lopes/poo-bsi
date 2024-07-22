class Usuario:
    def __init__(self):
        self.pontos = 0
        self.numeroDeArtigos = 0
    
    def setNumeroDeArtigos(self, nart):
        if isinstance(nart, int) and nart >= 0:
            self.numeroDeArtigos = nart
        else:
            raise ValueError("O número de artigos deve ser um inteiro não negativo.")
    
    def getNumeroDeArtigos(self):
        return self.numeroDeArtigos
    
    def calcPontuacao(self):
        raise NotImplementedError("Subclasses devem implementar este método.")


class Autor(Usuario):
    def calcPontuacao(self):
        self.pontos = self.numeroDeArtigos * 10 + 20
        return self.pontos


class Editor(Usuario):
    def calcPontuacao(self):
        self.pontos = self.numeroDeArtigos * 6 + 15
        return self.pontos


autor1 = Autor()
autor1.setNumeroDeArtigos(8)

editor1 = Editor()
editor1.setNumeroDeArtigos(15)
