from pycp2k.inputsection import InputSection
from ._each541 import _each541


class _forces5(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Add_last = None
        self.Common_iteration_levels = None
        self.Filename = None
        self.Log_print_key = None
        self.List = []
        self.Threshold = None
        self.EACH = _each541()
        self._name = "FORCES"
        self._keywords = {'Add_last': 'ADD_LAST', 'Common_iteration_levels': 'COMMON_ITERATION_LEVELS', 'Filename': 'FILENAME', 'Log_print_key': 'LOG_PRINT_KEY', 'Threshold': 'THRESHOLD'}
        self._repeated_keywords = {'List': 'LIST'}
        self._subsections = {'EACH': 'EACH'}
        self._attributes = ['Section_parameters']

