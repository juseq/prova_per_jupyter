"""
"""
from openpyxl import load_workbook
from openpyxl.drawing.image import Image

def load_cares_A_i_B():
    filename = 'fitxers/caresAiB.xlsx'

    try:
        wb = load_workbook(filename)
        returnCode = False
    except:
        print("Error al llegir el doc Excel")
        print(returnCode)
    else:
        caraA = wb['caraA']
        caraB = wb['caraB']

    return(wb, caraA, caraB)

def inserta_logo(full, imatge, h, w):
        logo = Image(imatge)
        logo.height = h
        logo.width = w
        full.add_image(logo, "A1")

def inserta_num_parte(parteA, parteB, n_parte, any):
    parteA["Y1"] = "{:0>4d}".format(n_parte) + '/' + any
    parteB["N1"] = "{:0>4d}".format(n_parte) + '/' + any

def inserta_data(parteA, parteB, avui, dema, encarregat):
    #veure si hi ha una data específica
    parteA["W4"] = dema.strftime("%d/%m/%Y")
    parteA["E25"] = avui.strftime("%d/%m/%Y")
    parteB["L3"] = dema.strftime("%d/%m/%Y")
    # insereix encarregat
    parteA["F24"].value = encarregat

def omple_comunicacions(parteA, parteB, operari):
    parteA["B9"] = 1011
    parteA["J9"] = 'C.C.'
    parteA["E6"] = 'Comunicaciones'
    #operaris
    parteA["G17"] = operari
    parteB["A8"] = operari