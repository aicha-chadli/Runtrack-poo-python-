class Animal:
    def __init__(self):
        """Constructeur pour initialiser l'attribut age à 0 et prenom à vide"""
        self.age = 0
        self.prenom = ""

    def vieillir(self):
        """Méthode qui fait vieillir l'animal en ajoutant 1 à son âge"""
        self.age += 1

    def nommer(self, prenom):
        """Méthode qui nomme l'animal en prenant le nom en paramètre"""
        self.prenom = prenom

    def afficherAge(self):
        """Méthode qui affiche l'âge de l'animal"""
        print(f"L'âge de l'animal est {self.age} ans")

    def afficherNom(self):
        """Méthode qui affiche le nom de l'animal"""
        print(f"L'animal se nomme {self.prenom}")


# Instanciation de l'objet Animal
animal1 = Animal()

# Affichage de l'âge initial
animal1.afficherAge()

# Faire vieillir l'animal et afficher l'âge mis à jour
animal1.vieillir()
animal1.afficherAge()

# Nommer l'animal et afficher son nom
animal1.nommer("Luna")
animal1.afficherNom()
