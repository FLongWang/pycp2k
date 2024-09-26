from pycp2k.inputsection import InputSection


class _gga_x_vmt84_ge6(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale = None
        self._name = "GGA_X_VMT84_GE"
        self._keywords = {'Scale': 'SCALE'}
        self._attributes = ['Section_parameters']

