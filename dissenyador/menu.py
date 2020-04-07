"""
menú del programa
"""
import helpers
import partes_per_dema as ppd
import excel_helper as xlh
import datetime
from datetime import date
import nom_equip as ne

# algunes dades
avui = date.today()
dema = avui + datetime.timedelta(days=1)
aquest_any = dema.strftime("%y")

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
    wb, cA, cB = xlh.load_cares_A_i_B()
    print("Fer els partes amb data de demà...\n")
    operaris_coms, operaris_vig, operacions_brigada, n_parte = ppd.load()  
    # comunicacions
    for oper in operaris_coms:
        print("**** parte per l'operador: {0} ****".format(oper))
        wb, n_parte = helpers.fes_parte(wb, cA, cB, n_parte, oper, avui, dema, aquest_any, 'comunicacions')
    print("++++++++++++++++++")

    # vigilància
    for oper in operaris_vig:
        print("**** parte pel vigilant: {0} ****".format(oper))
        wb, n_parte = helpers.fes_parte(wb, cA, cB, n_parte, oper, avui, dema, aquest_any, 'vigilància')
    print("++++++++++++++++++")

    # brigada
    for codi in operacions_brigada:
        helpers.salta(1)
        print("**** codi: {0} - ".format(codi) + " {1} ****".format(ne.equips[codi]))
        wb, n_parte = helpers.fes_parte(wb, cA, cB, n_parte, codi, avui, dema, aquest_any, 'brigada')
    print("++++++++++++++++++")

    helpers.desa_wb(wb, dema)

if option == '2':
    print("Fer els partes amb data d'avui...\n")
    wb, cA, cB = xlh.load_cares_A_i_B()
    operaris_coms, operaris_vig, operacions_brigada, n_parte = ppd.load()
    # brigada
    for codi in operacions_brigada:
        print("**** parte de brigada: {0} - {1} ****".format(codi, ne.equips[codi]))
        wb, n_parte = helpers.fes_parte(wb, cA, cB, n_parte, codi, avui, dema, aquest_any, 'brigada')
    print("Partes finalitzats")

    helpers.desa_wb(wb, dema)
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
