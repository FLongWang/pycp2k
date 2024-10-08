from pycp2k.inputsection import InputSection
from ._bias1 import _bias1
from ._model2 import _model2
from ._print75 import _print75


class _nnp2(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Nnp_input_file_name = None
        self.Scale_file_name = None
        self.BIAS = _bias1()
        self.MODEL_list = []
        self.PRINT = _print75()
        self._name = "NNP"
        self._keywords = {'Nnp_input_file_name': 'NNP_INPUT_FILE_NAME', 'Scale_file_name': 'SCALE_FILE_NAME'}
        self._subsections = {'BIAS': 'BIAS', 'PRINT': 'PRINT'}
        self._repeated_subsections = {'MODEL': '_model2'}
        self._attributes = ['MODEL_list']

    def MODEL_add(self, section_parameters=None):
        new_section = _model2()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.MODEL_list.append(new_section)
        return new_section

