"""
dissenyar els partes per demà
"""

import partes_coms as pc
import partes_vig as pv
import partes_brigada as pb

def load():
    print("Primer núm. de parte: ")
    primer_parte = int(input("> "))
    print("Primer parte: {0}".format(primer_parte))
    # coms
    opers_coms = pc.load()
    
    # vig
    opers_vig = pv.load()

    # brigada
    codis_brigada = pb.load()

    return(opers_coms, opers_vig, codis_brigada, primer_parte)