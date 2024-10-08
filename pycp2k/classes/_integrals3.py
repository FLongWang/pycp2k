from pycp2k.inputsection import InputSection
from ._eri_mme4 import _eri_mme4
from ._wfc_gpw3 import _wfc_gpw3
from ._interaction_potential11 import _interaction_potential11


class _integrals3(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Eri_method = None
        self.Size_lattice_sum = None
        self.ERI_MME = _eri_mme4()
        self.WFC_GPW = _wfc_gpw3()
        self.INTERACTION_POTENTIAL = _interaction_potential11()
        self._name = "INTEGRALS"
        self._keywords = {'Eri_method': 'ERI_METHOD', 'Size_lattice_sum': 'SIZE_LATTICE_SUM'}
        self._subsections = {'ERI_MME': 'ERI_MME', 'WFC_GPW': 'WFC_GPW', 'INTERACTION_POTENTIAL': 'INTERACTION_POTENTIAL'}

