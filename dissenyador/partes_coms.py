"""
partes comuicacions
"""
import helpers

def load():
    total_operaris = 0
    operadors = []
    operaris_coms = {
        '27' : 'Josep',
        '26' : 'Sandra',
        '28' : 'Joana',
        '29' : 'María',
        }

    while True:
        helpers.salta(2)
        print("******** COMUNICACIONS *********")
        print("\nEntrar nums. de comunicacions separats per espais: ")
        operaris = input("> ")
        operadors = operaris.split()
        total_operaris = len(operadors)
        print("\nPersonal de comunicacions: {0}".format(total_operaris))
        
        try:
            for opers in operadors: 
                print("Operador: {0}".format(operaris_coms[opers]))
            break
        except:
            print("\nERROR: l'operari no existeix...\n")

    #input("\nPrèmer ENTER per continuar...")
    return(operadors)
