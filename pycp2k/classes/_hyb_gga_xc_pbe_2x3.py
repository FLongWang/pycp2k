from pycp2k.inputsection import InputSection


class _hyb_gga_xc_pbe_2x3(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale = None
        self._beta = None
        self._name = "HYB_GGA_XC_PBE_2X"
        self._keywords = {'Scale': 'SCALE', '_beta': '_BETA'}
        self._attributes = ['Section_parameters']

