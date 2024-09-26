from pycp2k.inputsection import InputSection


class _mgga_x_ms2bs6(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale = None
        self._name = "MGGA_X_MS2BS"
        self._keywords = {'Scale': 'SCALE'}
        self._attributes = ['Section_parameters']

