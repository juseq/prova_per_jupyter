import nom_equip as ne
import helpers

total_operaris = 0
operaris = []
operaris_brigada = {
    '1' : 'Francesc',
    '2' : 'Edu',
    '3' : 'Kike',
    '4' : 'Palomo',
    '5' : '',
    '6' : '',
    '7' : '',
    '8' : '',
    '9' : 'Sisco',
    '10' : 'Jové',
    '11' : 'Mesa',
    '12' : '',
    '13' : '',
    '14' : '',
    '15' : '',
    '16' : '',
    '17' : '',
    '18' : '',
    '19' : '',
    '20' : '',
    }

def inserta_equip(caraA, codi):
    caraA["E6"] = ne.equips[codi]

def load_operarios_brigada(codi):

    while True:
        print("Entrar els codis dels operaris separats per espais: ")
        codis = input("> ")
        operaris = codis.split()
        total_operaris = len(operaris)
        print("\nOperaris: {0} ".format(total_operaris))
        
        try:
            for operari in operaris: 
                print("Operari: {0}".format(operaris_brigada[operari]))
            break
        except:
            print("\nERROR: l'operari no existeix...\n")
    helpers.salta()
    #input("\nPrèmer ENTER per continuar...")
    