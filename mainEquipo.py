from EquipoTec import Equipot
from Impresora import impresora

if __name__=='__main__':
    asus = Equipot(0, '', 0, '')
    asus.ElegirEquipo()

    hp = impresora(0, '', 0, '', '', '', 0)
    hp.elegirImpresora()


