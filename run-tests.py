import interp_Pvar
from utils import run_tests
import sys
sys.path.append("..")
import compiler

compiler = compiler.Compiler()

results = [run_tests("var", compiler, "var", None, interp_Pvar.InterpPvar().interp_P, None, None)]
if hasattr(compiler, "allocate_registers"):
    results.append(run_tests("regalloc", compiler, "regalloc", None, interp_Pvar.InterpPvar().interp_P, None, None))

if all(results):
    print("ALL TESTS PASSED! :D")
