from pycp2k.inputsection import InputSection
from ._bias_energy1 import _bias_energy1
from ._bias_forces1 import _bias_forces1


class _print74(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.BIAS_ENERGY = _bias_energy1()
        self.BIAS_FORCES = _bias_forces1()
        self._name = "PRINT"
        self._subsections = {'BIAS_ENERGY': 'BIAS_ENERGY', 'BIAS_FORCES': 'BIAS_FORCES'}

