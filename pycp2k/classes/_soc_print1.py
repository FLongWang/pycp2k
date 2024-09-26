from pycp2k.inputsection import InputSection
from ._each540 import _each540


class _soc_print1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Add_last = None
        self.Common_iteration_levels = None
        self.Filename = None
        self.Log_print_key = None
        self.Unit_ev = None
        self.Unit_wn = None
        self.Splitting = None
        self.Some = None
        self.EACH = _each540()
        self._name = "SOC_PRINT"
        self._keywords = {'Add_last': 'ADD_LAST', 'Common_iteration_levels': 'COMMON_ITERATION_LEVELS', 'Filename': 'FILENAME', 'Log_print_key': 'LOG_PRINT_KEY', 'Unit_ev': 'UNIT_EV', 'Unit_wn': 'UNIT_WN', 'Splitting': 'SPLITTING', 'Some': 'SOME'}
        self._subsections = {'EACH': 'EACH'}
        self._attributes = ['Section_parameters']

