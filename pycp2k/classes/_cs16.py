from pycp2k.inputsection import InputSection


class _cs16(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self._name = "CS1"
        self._attributes = ['Section_parameters']

