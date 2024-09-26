from pycp2k.inputsection import InputSection
from ._bse_iterat6 import _bse_iterat6


class _bse6(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Spin_config = None
        self.Bse_diag_method = None
        self.Bse_approx = None
        self.Energy_cutoff_occ = None
        self.Energy_cutoff_virt = None
        self.Bse_debug_print = None
        self.Num_print_exc = None
        self.Eps_x = None
        self.BSE_ITERAT = _bse_iterat6()
        self._name = "BSE"
        self._keywords = {'Spin_config': 'SPIN_CONFIG', 'Bse_diag_method': 'BSE_DIAG_METHOD', 'Bse_approx': 'BSE_APPROX', 'Energy_cutoff_occ': 'ENERGY_CUTOFF_OCC', 'Energy_cutoff_virt': 'ENERGY_CUTOFF_VIRT', 'Bse_debug_print': 'BSE_DEBUG_PRINT', 'Num_print_exc': 'NUM_PRINT_EXC', 'Eps_x': 'EPS_X'}
        self._subsections = {'BSE_ITERAT': 'BSE_ITERAT'}
        self._attributes = ['Section_parameters']

