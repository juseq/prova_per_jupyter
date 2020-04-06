"""
dissenyar els partes per demà
"""

import partes_coms as pc

def load():
    print("Primer núm. de parte: ")
    primer_parte = int(input("> "))
    total, opers = pc.load()
    print("Primer parte: {0}".format(primer_parte))
    return(total, opers, primer_parte)
