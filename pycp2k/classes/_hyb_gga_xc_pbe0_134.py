from pycp2k.inputsection import InputSection


class _hyb_gga_xc_pbe0_134(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale = None
        self._beta = None
        self._name = "HYB_GGA_XC_PBE0_13"
        self._keywords = {'Scale': 'SCALE', '_beta': '_BETA'}
        self._attributes = ['Section_parameters']

