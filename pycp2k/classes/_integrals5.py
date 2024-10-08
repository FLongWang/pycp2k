from pycp2k.inputsection import InputSection
from ._eri_mme7 import _eri_mme7
from ._wfc_gpw5 import _wfc_gpw5
from ._interaction_potential19 import _interaction_potential19


class _integrals5(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Eri_method = None
        self.Size_lattice_sum = None
        self.ERI_MME = _eri_mme7()
        self.WFC_GPW = _wfc_gpw5()
        self.INTERACTION_POTENTIAL = _interaction_potential19()
        self._name = "INTEGRALS"
        self._keywords = {'Eri_method': 'ERI_METHOD', 'Size_lattice_sum': 'SIZE_LATTICE_SUM'}
        self._subsections = {'ERI_MME': 'ERI_MME', 'WFC_GPW': 'WFC_GPW', 'INTERACTION_POTENTIAL': 'INTERACTION_POTENTIAL'}

