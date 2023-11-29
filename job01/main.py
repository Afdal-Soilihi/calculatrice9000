def saisie_nombre():
    while True:
        try:
            valeur = float(input("Entrez un nombre : "))
            return valeur
        except ValueError:
            print("Veuillez entrer un nombre valide.")

def saisie_operation():
    operations_valides = ['+', '-', '*', '/']
    while True:
        operation = input("Entrez une opération (+, -, *, /) : ")
        if operation in operations_valides:
            return operation
        else:
            print("Opération non valide. Veuillez réessayer.")

def calculatrice():
    try:
        nombre1 = saisie_nombre()
        nombre2 = saisie_nombre()
        operation = saisie_operation()

        if operation == '+':
            resultat = nombre1 + nombre2
        elif operation == '-':
            resultat = nombre1 - nombre2
        elif operation == '*':
            resultat = nombre1 * nombre2
        elif operation == '/':
            if nombre2 == 0:
                print("Erreur : division par zéro.")
                return
            else:
                resultat = nombre1 / nombre2

        print(f"Le résultat de {nombre1} {operation} {nombre2} est : {resultat}")

    except Exception as e:
        print(f"Une erreur est survenue : {e}")

if __name__ == "__main__":
    calculatrice()
    