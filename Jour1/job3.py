class Operation:
    def __init__(self, nombre1=0, nombre2=0):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

    def addition(self):
        resultat = self.nombre1 + self.nombre2
        print("Le résultat de l'addition est :", resultat)

# Création d'une instance de la classe avec les valeurs 12 et 3
operation_instance = Operation(12, 3)

# Affichage des valeurs des attributs
print("Le nombre1 est", operation_instance.nombre1)
print("Le nombre2 est", operation_instance.nombre2)

# Appel de la méthode addition()
operation_instance.addition()
