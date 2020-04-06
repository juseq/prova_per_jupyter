"""
"""
import os
import platform
import datetime
#import wx
from datetime import date
import excel_helper as xlh

# algunes dades
avui = date.today()
dema = avui + datetime.timedelta(days=1)
any = dema.strftime("%y")

def clear():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def omple_parte(n_parte, operari, wb, cA, cB):
    def entra_encarregat(name="M. Martín"):
        #pass
        return name       

    #cara A
    novaA = wb.copy_worksheet(cA)
    novaA.title = 'parte ' + "{:0>4d}".format(n_parte) + 'A'
    xlh.inserta_logo(novaA, "fitxers/logo-vector-becsa.png", 70, 190)
    
    #cara B
    novaB = wb.copy_worksheet(cB)
    novaB.title = 'parte ' + "{:0>4d}".format(n_parte) + 'B'
    xlh.inserta_logo(novaB, "fitxers/logo-vector-becsa.png", 70, 150)
    
    #comunicacions
    xlh.omple_comunicacions(novaA, novaB, operari)

    #dates i numeració
    xlh.inserta_num_parte(novaA, novaB, n_parte, any)
    encarregat = entra_encarregat()
    xlh.inserta_data(novaA, novaB, avui, dema, encarregat)

    return wb

def fes_parte(wb, cA, cB, n_parte, oper):
    wb = omple_parte(n_parte, oper, wb, cA, cB)
    
    n_parte += 1

    return(wb, n_parte)
       
def desa_wb(wb):
    wb.remove(wb['caraA'])
    wb.remove(wb['caraB'])
    wb.save(filename= dema.strftime("%d.%m.%Y") + ".xlsx")