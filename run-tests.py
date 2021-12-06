from utils import run_tests, enable_tracing
import interp_Pvar
import interp_Lif
import interp_Cif
import type_check_Lif
import type_check_Cif
import sys
sys.path.append("..")
import compiler

compiler = compiler.Compiler()


enable_tracing()
results = [run_tests("var", compiler, "var", None, interp_Pvar.InterpPvar().interp_P, None, None)]
if hasattr(compiler, "allocate_registers"):
    results.append(run_tests("regalloc", compiler, "regalloc", None, interp_Pvar.InterpPvar().interp_P, None, None))
if hasattr(compiler, "shrink"):
    results.append(run_tests("lif", compiler, "lif", type_check_Lif.TypeCheckLif().type_check, interp_Lif.InterpLif().interp, type_check_Cif.TypeCheckCif().type_check, interp_Cif.InterpCif().interp))

if all(results):
    print("ALL TESTS PASSED! :D")
