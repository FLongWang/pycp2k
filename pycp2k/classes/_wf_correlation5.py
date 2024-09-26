from pycp2k.inputsection import InputSection
from ._mp25 import _mp25
from ._ri_mp25 import _ri_mp25
from ._ri_rpa5 import _ri_rpa5
from ._ri_sos_mp25 import _ri_sos_mp25
from ._low_scaling5 import _low_scaling5
from ._ri19 import _ri19
from ._integrals5 import _integrals5
from ._canonical_gradients5 import _canonical_gradients5
from ._print96 import _print96


class _wf_correlation5(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Memory = None
        self.E_gap = None
        self.E_range = None
        self.Scale_s = None
        self.Scale_t = None
        self.Group_size = None
        self.MP2 = _mp25()
        self.RI_MP2 = _ri_mp25()
        self.RI_RPA = _ri_rpa5()
        self.RI_SOS_MP2 = _ri_sos_mp25()
        self.LOW_SCALING = _low_scaling5()
        self.RI = _ri19()
        self.INTEGRALS = _integrals5()
        self.CANONICAL_GRADIENTS = _canonical_gradients5()
        self.PRINT = _print96()
        self._name = "WF_CORRELATION"
        self._keywords = {'Memory': 'MEMORY', 'E_gap': 'E_GAP', 'E_range': 'E_RANGE', 'Scale_s': 'SCALE_S', 'Scale_t': 'SCALE_T', 'Group_size': 'GROUP_SIZE'}
        self._subsections = {'MP2': 'MP2', 'RI_MP2': 'RI_MP2', 'RI_RPA': 'RI_RPA', 'RI_SOS_MP2': 'RI_SOS_MP2', 'LOW_SCALING': 'LOW_SCALING', 'RI': 'RI', 'INTEGRALS': 'INTEGRALS', 'CANONICAL_GRADIENTS': 'CANONICAL_GRADIENTS', 'PRINT': 'PRINT'}
        self._aliases = {'Number_proc': 'Group_size'}


    @property
    def Number_proc(self):
        """
        See documentation for Group_size
        """
        return self.Group_size

    @Number_proc.setter
    def Number_proc(self, value):
        self.Group_size = value
