class Point:
    def __init__(self, x=0, y=0):
        """Constructeur pour initialiser les coordonnées x et y"""
        self.x = x
        self.y = y

    def afficherLesPoints(self):
        """Affiche les coordonnées x et y du point"""
        print(f"Coordonnées du point : ({self.x}, {self.y})")

    def afficherX(self):
        """Affiche la valeur de x"""
        print(f"Coordonnée x : {self.x}")

    def afficherY(self):
        """Affiche la valeur de y"""
        print(f"Coordonnée y : {self.y}")

    def changerX(self, nouvelle_valeur):
        """Change la valeur de x"""
        self.x = nouvelle_valeur

    def changerY(self, nouvelle_valeur):
        """Change la valeur de y"""
        self.y = nouvelle_valeur

# Exemple d'utilisation
point1 = Point(3, 4)

# Affichage des coordonnées
point1.afficherLesPoints()

# Affichage de x et y séparément
point1.afficherX()
point1.afficherY()

# Changement des coordonnées
point1.changerX(7)
point1.changerY(9)

# Affichage après changement
point1.afficherLesPoints()
point1.afficherX()
point1.afficherY()
