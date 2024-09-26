from pycp2k.inputsection import InputSection
from ._each339 import _each339


class _ibo_cubes1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Add_last = None
        self.Common_iteration_levels = None
        self.Filename = None
        self.Log_print_key = None
        self.Stride = None
        self.Append = None
        self.State_list = []
        self.EACH = _each339()
        self._name = "IBO_CUBES"
        self._keywords = {'Add_last': 'ADD_LAST', 'Common_iteration_levels': 'COMMON_ITERATION_LEVELS', 'Filename': 'FILENAME', 'Log_print_key': 'LOG_PRINT_KEY', 'Stride': 'STRIDE', 'Append': 'APPEND'}
        self._repeated_keywords = {'State_list': 'STATE_LIST'}
        self._subsections = {'EACH': 'EACH'}
        self._attributes = ['Section_parameters']

