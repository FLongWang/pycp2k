from pycp2k.inputsection import InputSection
from ._dos5 import _dos5


class _print121(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.DOS = _dos5()
        self._name = "PRINT"
        self._subsections = {'DOS': 'DOS'}

