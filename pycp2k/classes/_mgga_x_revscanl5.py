from pycp2k.inputsection import InputSection


class _mgga_x_revscanl5(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale = None
        self._c1 = None
        self._c2 = None
        self._d = None
        self._k1 = None
        self._a = None
        self._b = None
        self._name = "MGGA_X_REVSCANL"
        self._keywords = {'Scale': 'SCALE', '_c1': '_C1', '_c2': '_C2', '_d': '_D', '_k1': '_K1', '_a': '_A', '_b': '_B'}
        self._attributes = ['Section_parameters']

