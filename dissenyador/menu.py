"""
menú del programa
"""
import helpers
import partes_per_dema as ppd
import excel_helper as xlh

# os.system('clear')
helpers.clear()

print("========================================")
print("   BENVINGUT AL DISSENYADOR DE PARTES   ")
print("========================================")
print("[1] Fer els partes per demà             ")
print("[2] Fer els partes per avui             ")
print("[3] Fer parte de vialitat               ")
print("[4] Fer els partes d'una data concreta  ")
print("[5] canvi encarregat/preparat??         ")
print("[6] Sortir                              ")
print("========================================")

option = input("> ")

# os.system('clear')
helpers.clear()

if option == '1':
    print("Fer els partes amb data de demà...\n")
    total, operaris, n_parte = ppd.load()
    wb, cA, cB = xlh.load_cares_A_i_B()
    for oper in operaris:
        print("**** {0} ****".format(oper))
        wb, n_parte = helpers.fes_parte(wb, cA, cB, n_parte, oper)
        
    helpers.desa_wb(wb)

if option == '2':
    print("Fer els partes amb data d'avui...\n")
    # TODO
if option == '3':
    print("Fer parte de vialitat...\n")
    # TODO
if option == '4':
    print("Fer partes d'una data determinada...\n")
    # TODO
if option == '5':
    print("...\n")
    # TODO
if option == '6':
    print("Sortint...\n")
    

input("\nPrèmer ENTER per continuar...")
