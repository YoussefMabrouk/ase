"""This module defines an ASE interface to PACKMOL.

https://m3g.github.io/packmol/

Mainly intended to build initial geometry for MD simulations.

y.mabrouk@fz-juelich.de

Note : path to PACKMOL executable must be changed in function execute_packmol after installation

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
from test_ase.ase.io.proteindatabank import read_proteindatabank, write_proteindatabank

class Packmol(FileIOCalculator):
    """Class for doing Packmol calculations.
    """

    def __init__(self, label='SystemH_H2', molnames = ['H', 'H2'], 
                 molnumbers = [10, 10], molradii = [2.0, 2.0],
                 box = [37., 37., 37.], **kwargs):
        """Construct Packmol-calculator object.

        Parameters
        ==========
        molnumbers: list.
        molradii :  list.
        molnames : list.
        box : list
        """
        
        self.label = label
        self.molnames = molnames
        self.molnumbers = molnumbers
        self.molradii = molradii
        self.box = box

    def _execute_packmol(self):
        """ execute gmx command
        Parameters
        ----------
        command : str
        """
        print('execute')
        command = 'packmol-20.14.2/packmol < ' + self.label + '.inp'
        os.system(command)

    def run(self):
        """ runs a gromacs-mdrun with the
        current atom-configuration """
        print('run')
        self._execute_packmol()

    def write_input(self, atoms=None, properties=None, system_changes=None):
        """Write input parameters to input file."""
        
        with open(self.label+'.inp', 'w') as myfile:
            myfile.write('tolerance 2.0' + '\n')
            myfile.write('filetype pdb' + '\n')
            myfile.write('output ' + self.label+'.pdb' + '\n'*2)
            
            for i in range(len(self.molnames)):
                myfile.write('structure ' + self.molnames[i] + '.pdb' + '\n')
                myfile.write('  number ' + str(self.molnumbers[i]) + '\n')
                myfile.write('  inside box 2.0 2.0 2.0 {} {} {}'.format(self.box[0], self.box[1], self.box[2]) + '\n')
                myfile.write('  radius {}'.format(self.molradii[i]) + '\n')
                myfile.write('end structure' + '\n'*2)
                    
