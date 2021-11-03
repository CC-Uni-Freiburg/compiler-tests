import interp_Pvar
from utils import run_tests
import sys
sys.path.append("..")
import compiler

compiler = compiler.Compiler()

if run_tests("var", compiler, "var", None, interp_Pvar.InterpPvar().interp_P, None, None):
    print("ALL TESTS PASSED! :D")
