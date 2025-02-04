class Personne:
    def __init__(self, nom, prenom):
        """Constructeur de la classe Personne"""
        self.nom = nom
        self.prenom = prenom

    def SePresenter(self):
        """Méthode qui retourne le nom complet"""
        return f"Je suis {self.prenom} {self.nom}"

# Instanciation de plusieurs objets Personne
personne1 = Personne("Doe", "John")
personne2 = Personne("Dupond", "Jean")

# Affichage des présentations
print(personne1.SePresenter())
print(personne2.SePresenter())
