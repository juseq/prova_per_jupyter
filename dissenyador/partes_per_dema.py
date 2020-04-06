"""
dissenyar els partes per demà
"""

import partes_coms as pc
import partes_vig as pv

def load():
    print("Primer núm. de parte: ")
    primer_parte = int(input("> "))
    print("Primer parte: {0}".format(primer_parte))
    # coms
    opers_coms = pc.load()
    
    # vig
    opers_vig = pv.load()

    return(opers_coms, opers_vig, primer_parte)