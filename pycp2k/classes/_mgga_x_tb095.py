from pycp2k.inputsection import InputSection


class _mgga_x_tb095(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale = None
        self.C = None
        self._alpha = None
        self._name = "MGGA_X_TB09"
        self._keywords = {'Scale': 'SCALE', 'C': 'C', '_alpha': '_ALPHA'}
        self._attributes = ['Section_parameters']

