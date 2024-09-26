from pycp2k.inputsection import InputSection
from ._each537 import _each537


class _nto_analysis1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Add_last = None
        self.Common_iteration_levels = None
        self.Filename = None
        self.Log_print_key = None
        self.Threshold = None
        self.Intensity_threshold = None
        self.State_list = None
        self.Cube_files = None
        self.Stride = None
        self.Append = None
        self.EACH = _each537()
        self._name = "NTO_ANALYSIS"
        self._keywords = {'Add_last': 'ADD_LAST', 'Common_iteration_levels': 'COMMON_ITERATION_LEVELS', 'Filename': 'FILENAME', 'Log_print_key': 'LOG_PRINT_KEY', 'Threshold': 'THRESHOLD', 'Intensity_threshold': 'INTENSITY_THRESHOLD', 'State_list': 'STATE_LIST', 'Cube_files': 'CUBE_FILES', 'Stride': 'STRIDE', 'Append': 'APPEND'}
        self._subsections = {'EACH': 'EACH'}
        self._attributes = ['Section_parameters']

