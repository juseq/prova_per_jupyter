"""
partes de la brigada
"""

import nom_equip as ne

def load():
    # total_operaris = 0
    # operaris = []
    # operaris_brigada = {
    #     '1' : 'Francesc',
    #     '2' : 'Edu',
    #     '3' : 'Kike',
    #     '4' : 'Palomo',
    #     '5' : '',
    #     '6' : '',
    #     '7' : '',
    #     '8' : '',
    #     '9' : 'Sisco',
    #     '10' : 'Jové',
    #     '11' : 'Mesa',
    #     '12' : '',
    #     '13' : '',
    #     '14' : '',
    #     '15' : '',
    #     '16' : '',
    #     '17' : '',
    #     '18' : '',
    #     '19' : '',
    #     '20' : '',
    #     }

    while True:
        print("\nEntrar els codis de les operacions separats per espais: ")
        codis = input("> ")
        operacions = codis.split()
        total_operacions = len(operacions)
        print("\nOperacions introduïdes: {0} ".format(total_operacions))
        
        try:
            for operacio in operacions: 
                print("Operació: {0}".format(ne.equips[operacio]))
            break
        except:
            print("\nERROR: l'operació no existeix...\n")

    #input("\nPrèmer ENTER per continuar...")
    return(operacions)
