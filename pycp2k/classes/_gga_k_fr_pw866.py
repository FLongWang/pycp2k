from pycp2k.inputsection import InputSection


class _gga_k_fr_pw866(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale = None
        self._name = "GGA_K_FR_PW86"
        self._keywords = {'Scale': 'SCALE'}
        self._attributes = ['Section_parameters']

