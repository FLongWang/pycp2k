from pycp2k.inputsection import InputSection
from ._cphf10 import _cphf10


class _canonical_gradients5(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Eps_canonical = None
        self.Free_hfx_buffer = None
        self.Dot_product_blksize = None
        self.Max_parallel_comm = None
        self.CPHF = _cphf10()
        self._name = "CANONICAL_GRADIENTS"
        self._keywords = {'Eps_canonical': 'EPS_CANONICAL', 'Free_hfx_buffer': 'FREE_HFX_BUFFER', 'Dot_product_blksize': 'DOT_PRODUCT_BLKSIZE', 'Max_parallel_comm': 'MAX_PARALLEL_COMM'}
        self._subsections = {'CPHF': 'CPHF'}

