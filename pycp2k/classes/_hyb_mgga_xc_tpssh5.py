from pycp2k.inputsection import InputSection


class _hyb_mgga_xc_tpssh5(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale = None
        self._cx = None
        self._name = "HYB_MGGA_XC_TPSSH"
        self._keywords = {'Scale': 'SCALE', '_cx': '_CX'}
        self._attributes = ['Section_parameters']

