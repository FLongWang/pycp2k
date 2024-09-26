from pycp2k.inputsection import InputSection


class _hyb_gga_xc_apf6(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale = None
        self._name = "HYB_GGA_XC_APF"
        self._keywords = {'Scale': 'SCALE'}
        self._attributes = ['Section_parameters']

