class Animal:
    def __init__(self, nome, raca, cor):
        self.nome = nome
        self.raca = raca
        self.cor = cor
        
    def __str__(self):
        return f"{self.nome} - {self.raca} - {self.cor}"

class Tutor: 
    def __init__(self, nome, idade, estado):
        self.nome = nome
        self.idade = idade
        self.estado = estado
        self.lista_animais = []  # Inicializa a lista de animais
        self.lista_tutores = []  # Lista de tutores (não está sendo usada aqui)
        
    def adicionar_tutor(self, tutor):
        self.lista_tutores.append(tutor)
  
    def adicionar_animal(self, animal):
        self.lista_animais.append(animal)  # Adiciona o animal à lista de animais
    
    def __str__(self):
        return f"{self.nome}, {self.idade} anos, {self.estado}"

def main():
    # Criar tutores
    tutor1 = Tutor("Suzana", 23, "Santa Catarina")
    tutor2 = Tutor("Felipe", 50, "Cuiabá")
    
    # Criar animais
    animal1 = Animal("Rex", "Beagle", "Branco")
    animal2 = Animal("Bolinha", "Vira-lata", "Caramelo")
    
    # Adicionar animais aos tutores
    tutor1.adicionar_animal(animal1)
    tutor2.adicionar_animal(animal2)
    
    # Exibir tutores e seus animais
    for tutor in [tutor1, tutor2]:
        print(f"Tutor: {tutor}")
        for animal in tutor.lista_animais:
            print(f"  Animal: {animal}")

if __name__ == "__main__":
    main()