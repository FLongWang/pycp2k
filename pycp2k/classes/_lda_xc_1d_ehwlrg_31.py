from pycp2k.inputsection import InputSection


class _lda_xc_1d_ehwlrg_31(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale = None
        self._name = "LDA_XC_1D_EHWLRG_3"
        self._keywords = {'Scale': 'SCALE'}
        self._attributes = ['Section_parameters']

