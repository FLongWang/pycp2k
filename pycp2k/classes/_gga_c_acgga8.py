from pycp2k.inputsection import InputSection


class _gga_c_acgga8(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale = None
        self._name = "GGA_C_ACGGA"
        self._keywords = {'Scale': 'SCALE'}
        self._attributes = ['Section_parameters']

