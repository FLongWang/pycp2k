from pycp2k.inputsection import InputSection
from ._local_bandgap7 import _local_bandgap7
from ._gw_dos7 import _gw_dos7


class _print128(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.LOCAL_BANDGAP = _local_bandgap7()
        self.GW_DOS = _gw_dos7()
        self._name = "PRINT"
        self._subsections = {'LOCAL_BANDGAP': 'LOCAL_BANDGAP', 'GW_DOS': 'GW_DOS'}

