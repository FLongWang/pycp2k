from pycp2k.inputsection import InputSection
from ._ri_info18 import _ri_info18
from ._ri_density_coeffs18 import _ri_density_coeffs18
from ._ri_metric_2c_ints18 import _ri_metric_2c_ints18


class _print114(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.RI_INFO = _ri_info18()
        self.RI_DENSITY_COEFFS = _ri_density_coeffs18()
        self.RI_METRIC_2C_INTS = _ri_metric_2c_ints18()
        self._name = "PRINT"
        self._subsections = {'RI_INFO': 'RI_INFO', 'RI_DENSITY_COEFFS': 'RI_DENSITY_COEFFS', 'RI_METRIC_2C_INTS': 'RI_METRIC_2C_INTS'}

