"""This module defines an ASE interface to RSMD.

https://github.com/myrabiedermann/rsmd

Mainly intended to start RSMD simulations once the input files were already generated.

y.mabrouk@fz-juelich.de

Notes : 
Path to RSMD executable needs to be changed in _execute_rsmd() function after the installation.
A function to read RSMD ouput and convert it to class Atoms needs to be written.

"""

import os
import subprocess
from glob import glob
from shutil import which

import numpy as np

from ase import units
from ase.calculators.calculator import (EnvironmentError,
                                        FileIOCalculator,
                                        all_changes)
#from test_ase.ase.io.rsmd import read_rsmd, write_rsmd

class RSMD(FileIOCalculator):
    """Class for doing RSMD calculations.
    """
    def __init__(self, ncycles='10', nsteps='100', **kwargs):
        """Construct RSMD-calculator object.
        Parameters
        ==========
        """
        
    def write_input():
        
        for (FileName, ParameterName, Parameter) in ("INPUT", "ncycles", ncycles), ("cycle.mdp", "nsteps", nsteps):
            InputFile = open(FileName).readlines()
            ParamLine = InputFile.index([Line for Line in InputFile if Parameter in Line][0])
            InputFile[ParamLine] = Parameter + "     = " + str(int(WanoFile["Parameters"][0][Parameter])) + " \n"
            
            with open(FileName, "w") as Line:
                for LinePrime in InputFile:
                    Line.write(LinePrime) 

    def _execute_rsmd(self):
        """ execute rs@md command
        Parameters
        ----------
        command : str
        """
        os.system("rsmd/build/rsmd -i INPUT")

    def run(self):
        """ runs a rsmd with the
        current atom-configuration """
        self._execute_rsmd()
