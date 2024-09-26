from pycp2k.inputsection import InputSection
from ._hf_info10 import _hf_info10
from ._periodic10 import _periodic10
from ._screening11 import _screening11
from ._interaction_potential13 import _interaction_potential13
from ._load_balance10 import _load_balance10
from ._memory11 import _memory11
from ._ri13 import _ri13


class _hf10(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Fraction = None
        self.Treat_lsd_in_core = None
        self.Pw_hfx = None
        self.Pw_hfx_blocksize = None
        self.HF_INFO = _hf_info10()
        self.PERIODIC = _periodic10()
        self.SCREENING = _screening11()
        self.INTERACTION_POTENTIAL = _interaction_potential13()
        self.LOAD_BALANCE = _load_balance10()
        self.MEMORY = _memory11()
        self.RI = _ri13()
        self._name = "HF"
        self._keywords = {'Fraction': 'FRACTION', 'Treat_lsd_in_core': 'TREAT_LSD_IN_CORE', 'Pw_hfx': 'PW_HFX', 'Pw_hfx_blocksize': 'PW_HFX_BLOCKSIZE'}
        self._subsections = {'HF_INFO': 'HF_INFO', 'PERIODIC': 'PERIODIC', 'SCREENING': 'SCREENING', 'INTERACTION_POTENTIAL': 'INTERACTION_POTENTIAL', 'LOAD_BALANCE': 'LOAD_BALANCE', 'MEMORY': 'MEMORY', 'RI': 'RI'}

