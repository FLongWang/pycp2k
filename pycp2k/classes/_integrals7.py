from pycp2k.inputsection import InputSection
from ._eri_mme9 import _eri_mme9
from ._wfc_gpw7 import _wfc_gpw7
from ._interaction_potential27 import _interaction_potential27


class _integrals7(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Eri_method = None
        self.Size_lattice_sum = None
        self.ERI_MME = _eri_mme9()
        self.WFC_GPW = _wfc_gpw7()
        self.INTERACTION_POTENTIAL = _interaction_potential27()
        self._name = "INTEGRALS"
        self._keywords = {'Eri_method': 'ERI_METHOD', 'Size_lattice_sum': 'SIZE_LATTICE_SUM'}
        self._subsections = {'ERI_MME': 'ERI_MME', 'WFC_GPW': 'WFC_GPW', 'INTERACTION_POTENTIAL': 'INTERACTION_POTENTIAL'}

