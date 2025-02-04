class Operation:
    def __init__(self, nombre1=0, nombre2=0):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

# Instanciation de la classe avec les valeurs demandées
operation_instance = Operation(12, 3)

# Affichage des valeurs des attributs
print("Le nombre1 est", operation_instance.nombre1)
print("Le nombre2 est", operation_instance.nombre2)
feat: Ajout de la classe Operation avec affichage des attributs