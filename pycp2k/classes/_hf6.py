from pycp2k.inputsection import InputSection
from ._hf_info6 import _hf_info6
from ._periodic6 import _periodic6
from ._screening6 import _screening6
from ._interaction_potential8 import _interaction_potential8
from ._load_balance6 import _load_balance6
from ._memory6 import _memory6
from ._ri8 import _ri8


class _hf6(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Fraction = None
        self.Treat_lsd_in_core = None
        self.Pw_hfx = None
        self.Pw_hfx_blocksize = None
        self.HF_INFO = _hf_info6()
        self.PERIODIC = _periodic6()
        self.SCREENING = _screening6()
        self.INTERACTION_POTENTIAL = _interaction_potential8()
        self.LOAD_BALANCE = _load_balance6()
        self.MEMORY = _memory6()
        self.RI = _ri8()
        self._name = "HF"
        self._keywords = {'Fraction': 'FRACTION', 'Treat_lsd_in_core': 'TREAT_LSD_IN_CORE', 'Pw_hfx': 'PW_HFX', 'Pw_hfx_blocksize': 'PW_HFX_BLOCKSIZE'}
        self._subsections = {'HF_INFO': 'HF_INFO', 'PERIODIC': 'PERIODIC', 'SCREENING': 'SCREENING', 'INTERACTION_POTENTIAL': 'INTERACTION_POTENTIAL', 'LOAD_BALANCE': 'LOAD_BALANCE', 'MEMORY': 'MEMORY', 'RI': 'RI'}

