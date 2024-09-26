from pycp2k.inputsection import InputSection
from ._each337 import _each337


class _charge_center1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Add_last = None
        self.Common_iteration_levels = None
        self.Filename = None
        self.Log_print_key = None
        self.Position_operator_berry = None
        self.EACH = _each337()
        self._name = "CHARGE_CENTER"
        self._keywords = {'Add_last': 'ADD_LAST', 'Common_iteration_levels': 'COMMON_ITERATION_LEVELS', 'Filename': 'FILENAME', 'Log_print_key': 'LOG_PRINT_KEY', 'Position_operator_berry': 'POSITION_OPERATOR_BERRY'}
        self._subsections = {'EACH': 'EACH'}
        self._attributes = ['Section_parameters']

