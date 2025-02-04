class Personnage:
    def __init__(self, x=0, y=0):
        """Constructeur pour initialiser la position du personnage"""
        self.x = x
        self.y = y

    def gauche(self):
        """Déplace le personnage vers la gauche (diminution de x)"""
        self.x -= 1

    def droite(self):
        """Déplace le personnage vers la droite (augmentation de x)"""
        self.x += 1

    def haut(self):
        """Déplace le personnage vers le haut (diminution de y)"""
        self.y -= 1

    def bas(self):
        """Déplace le personnage vers le bas (augmentation de y)"""
        self.y += 1

    def position(self):
        """Retourne la position sous forme de tuple (x, y)"""
        return (self.x, self.y)

# Exemple d'utilisation
personnage = Personnage(2, 3)

# Affichage de la position initiale
print("Position initiale :", personnage.position())

# Déplacer le personnage et afficher sa nouvelle position
personnage.gauche()
personnage.haut()
print("Nouvelle position :", personnage.position())

# Déplacer encore le personnage et afficher sa position
personnage.droite()
personnage.bas()
print("Position après déplacement :", personnage.position())
