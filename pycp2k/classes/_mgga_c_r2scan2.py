from pycp2k.inputsection import InputSection


class _mgga_c_r2scan2(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale = None
        self._eta = None
        self._name = "MGGA_C_R2SCAN"
        self._keywords = {'Scale': 'SCALE', '_eta': '_ETA'}
        self._attributes = ['Section_parameters']

