from pycp2k.inputsection import InputSection
from ._restart18 import _restart18


class _zmp1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.File_density = None
        self.Grid_tol = None
        self.Lambda = None
        self.Dm = None
        self.RESTART = _restart18()
        self._name = "ZMP"
        self._keywords = {'File_density': 'FILE_DENSITY', 'Grid_tol': 'GRID_TOL', 'Lambda': 'LAMBDA', 'Dm': 'DM'}
        self._subsections = {'RESTART': 'RESTART'}

