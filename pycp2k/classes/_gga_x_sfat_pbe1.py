from pycp2k.inputsection import InputSection


class _gga_x_sfat_pbe1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale = None
        self._omega = None
        self._name = "GGA_X_SFAT_PBE"
        self._keywords = {'Scale': 'SCALE', '_omega': '_OMEGA'}
        self._attributes = ['Section_parameters']

