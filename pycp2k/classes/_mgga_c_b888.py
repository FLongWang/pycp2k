from pycp2k.inputsection import InputSection


class _mgga_c_b888(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale = None
        self._name = "MGGA_C_B88"
        self._keywords = {'Scale': 'SCALE'}
        self._attributes = ['Section_parameters']

