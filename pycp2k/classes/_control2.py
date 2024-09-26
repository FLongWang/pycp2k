from pycp2k.inputsection import InputSection


class _control2(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Beta_chunk_size = None
        self.Beta_on_device = None
        self.Cyclic_block_size = None
        self.Fft_mode = None
        self.Gen_evp_solver_name = None
        self.Gvec_chunk_size = None
        self.Mpi_grid_dims = None
        self.Num_bands_to_print = None
        self.Ortho_rf = None
        self.Output = None
        self.Print_forces = None
        self.Print_neighbors = None
        self.Print_stress = None
        self.Processing_unit = None
        self.Reduce_gvec = None
        self.Rmt_max = None
        self.Save_rf = None
        self.Spglib_tolerance = None
        self.Std_evp_solver_name = None
        self.Use_second_variation = None
        self.Verbosity = None
        self.Verification = None
        self._name = "CONTROL"
        self._keywords = {'Beta_chunk_size': 'BETA_CHUNK_SIZE', 'Beta_on_device': 'BETA_ON_DEVICE', 'Cyclic_block_size': 'CYCLIC_BLOCK_SIZE', 'Fft_mode': 'FFT_MODE', 'Gen_evp_solver_name': 'GEN_EVP_SOLVER_NAME', 'Gvec_chunk_size': 'GVEC_CHUNK_SIZE', 'Mpi_grid_dims': 'MPI_GRID_DIMS', 'Num_bands_to_print': 'NUM_BANDS_TO_PRINT', 'Ortho_rf': 'ORTHO_RF', 'Output': 'OUTPUT', 'Print_forces': 'PRINT_FORCES', 'Print_neighbors': 'PRINT_NEIGHBORS', 'Print_stress': 'PRINT_STRESS', 'Processing_unit': 'PROCESSING_UNIT', 'Reduce_gvec': 'REDUCE_GVEC', 'Rmt_max': 'RMT_MAX', 'Save_rf': 'SAVE_RF', 'Spglib_tolerance': 'SPGLIB_TOLERANCE', 'Std_evp_solver_name': 'STD_EVP_SOLVER_NAME', 'Use_second_variation': 'USE_SECOND_VARIATION', 'Verbosity': 'VERBOSITY', 'Verification': 'VERIFICATION'}

