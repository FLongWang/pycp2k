from pycp2k.inputsection import InputSection
from ._lennard_jones1 import _lennard_jones1
from ._williams1 import _williams1
from ._eam1 import _eam1
from ._quip1 import _quip1
from ._nequip1 import _nequip1
from ._allegro1 import _allegro1
from ._deepmd1 import _deepmd1
from ._goodwin1 import _goodwin1
from ._ipbv1 import _ipbv1
from ._bmhft1 import _bmhft1
from ._bmhftd1 import _bmhftd1
from ._buck4ranges1 import _buck4ranges1
from ._buckmorse1 import _buckmorse1
from ._genpot2 import _genpot2
from ._tersoff1 import _tersoff1
from ._siepmann1 import _siepmann1
from ._gal191 import _gal191
from ._gal211 import _gal211
from ._tabpot1 import _tabpot1


class _nonbonded2(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.LENNARD_JONES_list = []
        self.WILLIAMS_list = []
        self.EAM_list = []
        self.QUIP_list = []
        self.NEQUIP = _nequip1()
        self.ALLEGRO = _allegro1()
        self.DEEPMD = _deepmd1()
        self.GOODWIN_list = []
        self.IPBV_list = []
        self.BMHFT_list = []
        self.BMHFTD_list = []
        self.BUCK4RANGES_list = []
        self.BUCKMORSE_list = []
        self.GENPOT_list = []
        self.TERSOFF_list = []
        self.SIEPMANN_list = []
        self.GAL19_list = []
        self.GAL21_list = []
        self.TABPOT_list = []
        self._name = "NONBONDED"
        self._subsections = {'NEQUIP': 'NEQUIP', 'ALLEGRO': 'ALLEGRO', 'DEEPMD': 'DEEPMD'}
        self._repeated_subsections = {'LENNARD_JONES': '_lennard_jones1', 'WILLIAMS': '_williams1', 'EAM': '_eam1', 'QUIP': '_quip1', 'GOODWIN': '_goodwin1', 'IPBV': '_ipbv1', 'BMHFT': '_bmhft1', 'BMHFTD': '_bmhftd1', 'BUCK4RANGES': '_buck4ranges1', 'BUCKMORSE': '_buckmorse1', 'GENPOT': '_genpot2', 'TERSOFF': '_tersoff1', 'SIEPMANN': '_siepmann1', 'GAL19': '_gal191', 'GAL21': '_gal211', 'TABPOT': '_tabpot1'}
        self._attributes = ['LENNARD_JONES_list', 'WILLIAMS_list', 'EAM_list', 'QUIP_list', 'GOODWIN_list', 'IPBV_list', 'BMHFT_list', 'BMHFTD_list', 'BUCK4RANGES_list', 'BUCKMORSE_list', 'GENPOT_list', 'TERSOFF_list', 'SIEPMANN_list', 'GAL19_list', 'GAL21_list', 'TABPOT_list']

    def LENNARD_JONES_add(self, section_parameters=None):
        new_section = _lennard_jones1()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.LENNARD_JONES_list.append(new_section)
        return new_section

    def WILLIAMS_add(self, section_parameters=None):
        new_section = _williams1()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.WILLIAMS_list.append(new_section)
        return new_section

    def EAM_add(self, section_parameters=None):
        new_section = _eam1()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.EAM_list.append(new_section)
        return new_section

    def QUIP_add(self, section_parameters=None):
        new_section = _quip1()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.QUIP_list.append(new_section)
        return new_section

    def GOODWIN_add(self, section_parameters=None):
        new_section = _goodwin1()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.GOODWIN_list.append(new_section)
        return new_section

    def IPBV_add(self, section_parameters=None):
        new_section = _ipbv1()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.IPBV_list.append(new_section)
        return new_section

    def BMHFT_add(self, section_parameters=None):
        new_section = _bmhft1()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.BMHFT_list.append(new_section)
        return new_section

    def BMHFTD_add(self, section_parameters=None):
        new_section = _bmhftd1()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.BMHFTD_list.append(new_section)
        return new_section

    def BUCK4RANGES_add(self, section_parameters=None):
        new_section = _buck4ranges1()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.BUCK4RANGES_list.append(new_section)
        return new_section

    def BUCKMORSE_add(self, section_parameters=None):
        new_section = _buckmorse1()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.BUCKMORSE_list.append(new_section)
        return new_section

    def GENPOT_add(self, section_parameters=None):
        new_section = _genpot2()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.GENPOT_list.append(new_section)
        return new_section

    def TERSOFF_add(self, section_parameters=None):
        new_section = _tersoff1()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.TERSOFF_list.append(new_section)
        return new_section

    def SIEPMANN_add(self, section_parameters=None):
        new_section = _siepmann1()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.SIEPMANN_list.append(new_section)
        return new_section

    def GAL19_add(self, section_parameters=None):
        new_section = _gal191()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.GAL19_list.append(new_section)
        return new_section

    def GAL21_add(self, section_parameters=None):
        new_section = _gal211()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.GAL21_list.append(new_section)
        return new_section

    def TABPOT_add(self, section_parameters=None):
        new_section = _tabpot1()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.TABPOT_list.append(new_section)
        return new_section

