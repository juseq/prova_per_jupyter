"""
partes de la brigada
"""
import helpers
import nom_equip as ne

def load():
    while True:
        helpers.salta(2)
        print("******** BRIGADA *********")
        print("\nEntrar els codis de les operacions separats per espais: ")
        codis = input("> ")
        operacions = codis.split()
        total_operacions = len(operacions)
        helpers.salta()
        print("Operacions introduïdes: {0} ".format(total_operacions))
        
        try:
            for operacio in operacions: 
                print("Operació: {0}".format(ne.equips[operacio]))
            break
        except:
            print("\nERROR: l'operació no existeix...\n")
    
    helpers.salta()
    #input("\nPrèmer ENTER per continuar...")
    return(operacions)
