from pycp2k.inputsection import InputSection


class _gga_k_gds087(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale = None
        self._name = "GGA_K_GDS08"
        self._keywords = {'Scale': 'SCALE'}
        self._attributes = ['Section_parameters']

