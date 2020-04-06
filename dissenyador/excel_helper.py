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

def inserta_num_parte(caraA, caraB, n_parte, any):
    caraA["Y1"] = "{:0>4d}".format(n_parte) + '/' + any
    caraB["N1"] = "{:0>4d}".format(n_parte) + '/' + any

def inserta_data(caraA, caraB, avui, dema, encarregat):
    #veure si hi ha una data específica
    caraA["W4"] = dema.strftime("%d/%m/%Y")
    caraA["E25"] = avui.strftime("%d/%m/%Y")
    caraB["L3"] = dema.strftime("%d/%m/%Y")
    # insereix encarregat
    caraA["F24"].value = encarregat

def omple_comunicacions(caraA, caraB, operari):
    caraA["B9"] = 1011
    caraA["J9"] = 'C.C.'
    caraA["E6"] = 'Comunicaciones'
    #operaris
    caraA["G17"] = operari
    caraB["A8"] = operari

def omple_vigilants(caraA, caraB, operari):
    caraA["B9"] = 1013
    caraA["J9"] = 'T.S.'
    caraA["E6"] = 'Vigilancia'
    caraA["B13"] = 30002
    caraA["D13"] = "Atención a incidencias fuera del horario laboral"
    caraB["A17"] = 203
    #operaris
    caraA["G17"] = operari
    caraB["A8"] = operari