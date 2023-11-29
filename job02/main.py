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
    historique = []

    try:
        while True:
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
                    continue
                else:
                    resultat = nombre1 / nombre2

            operation_str = f"{nombre1} {operation} {nombre2} = {resultat}"
            historique.append(operation_str)

            print(f"Le résultat de {operation_str}")

            continuer = input("Voulez-vous effectuer une autre opération ? (O/N) : ").upper()
            if continuer != 'O':
                break

        afficher_historique(historique)

    except Exception as e:
        print(f"Une erreur est survenue : {e}")

def afficher_historique(historique):
    print("\nHistorique des opérations :")
    for operation in historique:
        print(operation)

    effacer = input("Voulez-vous effacer l'historique ? (O/N) : ").upper()
    if effacer == 'O':
        historique.clear()
        print("L'historique a été effacé.")

if __name__ == "__main__":
    calculatrice()