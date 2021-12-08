import os
import sys
from sys import platform
import ast
from filecmp import cmp
from ast import *

import interp_Pvar
import interp_Lif
import interp_Cif
import type_check_Lif
import type_check_Cif
import sys
sys.path.append("..")

trace = print

def run_interpreter(type_check_P, interp_P, program_filename):
    
    program_root = program_filename.split(".")[0]
    with open(program_filename) as source:
        program = parse(source.read())

    trace("\n***************\n source program \n***************\n")
    trace(program)
    trace("")

    trace("\n***************\n type check     \n***************\n")
    if type_check_P:
        type_check_P(program)

    interp_P (program)

def run_Lif (program_filename):
    run_interpreter (
        type_check_Lif.TypeCheckLif().type_check,
        interp_Lif.InterpLif().interp,
        program_filename)
