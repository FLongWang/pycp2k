from pycp2k.inputsection import InputSection
from ._program_run_info49 import _program_run_info49
from ._dos6 import _dos6
from ._transmission1 import _transmission1


class _print122(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.PROGRAM_RUN_INFO = _program_run_info49()
        self.DOS = _dos6()
        self.TRANSMISSION = _transmission1()
        self._name = "PRINT"
        self._subsections = {'PROGRAM_RUN_INFO': 'PROGRAM_RUN_INFO', 'DOS': 'DOS', 'TRANSMISSION': 'TRANSMISSION'}

