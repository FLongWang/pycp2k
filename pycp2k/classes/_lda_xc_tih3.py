from pycp2k.inputsection import InputSection


class _lda_xc_tih3(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale = None
        self._name = "LDA_XC_TIH"
        self._keywords = {'Scale': 'SCALE'}
        self._attributes = ['Section_parameters']

