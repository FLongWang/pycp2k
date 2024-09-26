from pycp2k.inputsection import InputSection


class _mgga_x_ms2b3(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale = None
        self._name = "MGGA_X_MS2B"
        self._keywords = {'Scale': 'SCALE'}
        self._attributes = ['Section_parameters']

