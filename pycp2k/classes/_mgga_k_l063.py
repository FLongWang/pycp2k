from pycp2k.inputsection import InputSection


class _mgga_k_l063(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale = None
        self._kappa = None
        self._name = "MGGA_K_L06"
        self._keywords = {'Scale': 'SCALE', '_kappa': '_KAPPA'}
        self._attributes = ['Section_parameters']

