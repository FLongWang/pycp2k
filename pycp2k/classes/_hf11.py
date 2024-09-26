from pycp2k.inputsection import InputSection
from ._hf_info11 import _hf_info11
from ._periodic11 import _periodic11
from ._screening12 import _screening12
from ._interaction_potential14 import _interaction_potential14
from ._load_balance11 import _load_balance11
from ._memory12 import _memory12
from ._ri14 import _ri14


class _hf11(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Fraction = None
        self.Treat_lsd_in_core = None
        self.Pw_hfx = None
        self.Pw_hfx_blocksize = None
        self.HF_INFO = _hf_info11()
        self.PERIODIC = _periodic11()
        self.SCREENING = _screening12()
        self.INTERACTION_POTENTIAL = _interaction_potential14()
        self.LOAD_BALANCE = _load_balance11()
        self.MEMORY = _memory12()
        self.RI = _ri14()
        self._name = "HF"
        self._keywords = {'Fraction': 'FRACTION', 'Treat_lsd_in_core': 'TREAT_LSD_IN_CORE', 'Pw_hfx': 'PW_HFX', 'Pw_hfx_blocksize': 'PW_HFX_BLOCKSIZE'}
        self._subsections = {'HF_INFO': 'HF_INFO', 'PERIODIC': 'PERIODIC', 'SCREENING': 'SCREENING', 'INTERACTION_POTENTIAL': 'INTERACTION_POTENTIAL', 'LOAD_BALANCE': 'LOAD_BALANCE', 'MEMORY': 'MEMORY', 'RI': 'RI'}

