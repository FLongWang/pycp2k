from pycp2k.inputsection import InputSection


class _hyb_mgga_xc_mpwkcis1k2(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale = None
        self._name = "HYB_MGGA_XC_MPWKCIS1K"
        self._keywords = {'Scale': 'SCALE'}
        self._attributes = ['Section_parameters']

