"""
"""
import os
import platform
import excel_helper as xlh

def clear():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def salta(salts=1):
    for i in range(salts):
        print("\n")

def omple_parte(n_parte, oparari_o_codi, wb, cA, cB, avui, dema, aquest_any, section):
    def entra_encarregat(name="M. Martín"):
        #TODO
        return name       

    #cara A
    novaA = wb.copy_worksheet(cA)
    novaA.title = 'parte ' + "{:0>4d}".format(n_parte) + 'A'
    xlh.inserta_logo(novaA, "fitxers/logo-vector-becsa.png", 70, 190)
    
    #cara B
    novaB = wb.copy_worksheet(cB)
    novaB.title = 'parte ' + "{:0>4d}".format(n_parte) + 'B'
    xlh.inserta_logo(novaB, "fitxers/logo-vector-becsa.png", 70, 150)
    
    # secció?
    if section == 'comunicacions':
        xlh.omple_comunicacions(novaA, novaB, oparari_o_codi)
    elif section == 'vigilància':
        xlh.omple_vigilants(novaA, novaB, oparari_o_codi)
    elif section == 'brigada':
        xlh.omple_brigada(novaA, novaB, oparari_o_codi)

    #dates i numeració
    xlh.inserta_num_parte(novaA, novaB, n_parte, aquest_any)
    encarregat = entra_encarregat()
    xlh.inserta_data(novaA, novaB, avui, dema, encarregat)

    return wb

def fes_parte(wb, cA, cB, n_parte, oper, avui, dema, aquest_any, section):
    wb = omple_parte(n_parte, oper, wb, cA, cB, avui, dema, aquest_any, section)
    
    n_parte += 1

    return(wb, n_parte)
       
def desa_wb(wb, dia):
    wb.remove(wb['caraA'])
    wb.remove(wb['caraB'])
    wb.save(filename= dia.strftime("%d.%m.%Y") + ".xlsx")