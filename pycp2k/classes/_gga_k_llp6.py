from pycp2k.inputsection import InputSection


class _gga_k_llp6(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale = None
        self._name = "GGA_K_LLP"
        self._keywords = {'Scale': 'SCALE'}
        self._attributes = ['Section_parameters']

