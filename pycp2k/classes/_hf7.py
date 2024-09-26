from pycp2k.inputsection import InputSection
from ._hf_info7 import _hf_info7
from ._periodic7 import _periodic7
from ._screening8 import _screening8
from ._interaction_potential9 import _interaction_potential9
from ._load_balance7 import _load_balance7
from ._memory8 import _memory8
from ._ri9 import _ri9


class _hf7(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Fraction = None
        self.Treat_lsd_in_core = None
        self.Pw_hfx = None
        self.Pw_hfx_blocksize = None
        self.HF_INFO = _hf_info7()
        self.PERIODIC = _periodic7()
        self.SCREENING = _screening8()
        self.INTERACTION_POTENTIAL = _interaction_potential9()
        self.LOAD_BALANCE = _load_balance7()
        self.MEMORY = _memory8()
        self.RI = _ri9()
        self._name = "HF"
        self._keywords = {'Fraction': 'FRACTION', 'Treat_lsd_in_core': 'TREAT_LSD_IN_CORE', 'Pw_hfx': 'PW_HFX', 'Pw_hfx_blocksize': 'PW_HFX_BLOCKSIZE'}
        self._subsections = {'HF_INFO': 'HF_INFO', 'PERIODIC': 'PERIODIC', 'SCREENING': 'SCREENING', 'INTERACTION_POTENTIAL': 'INTERACTION_POTENTIAL', 'LOAD_BALANCE': 'LOAD_BALANCE', 'MEMORY': 'MEMORY', 'RI': 'RI'}

