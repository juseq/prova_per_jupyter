"""
partes vigilància
"""

def load():
    total_vigilants = 0
    vigilants = []
    operaris_vigilancia = {
        '24' : 'Matías',
        '21' : 'Víctor',
        '22' : 'Gual',
        '17' : 'Moisés',
        '23' : 'Padilla',
        '1' : 'Francesc',
        '9' : 'Sisco',
        '10' : 'Jové',
        '11' : 'Mesa',
        '3' : 'Kike',
        }

    while True:
        print("\nEntrar nums. dels vigilants separats per espais: ")
        operaris = input("> ")
        vigilants = operaris.split()
        total_vigilants = len(vigilants)
        print("\nPersonal de vigilància: {0}".format(total_vigilants))
        
        try:
            for opers in vigilants: 
                print("Vigilant: {0}".format(operaris_vigilancia[opers]))
            break
        except:
            print("\nERROR: l'operari no existeix...\n")

    #input("\nPrèmer ENTER per continuar...")
    return(vigilants)
