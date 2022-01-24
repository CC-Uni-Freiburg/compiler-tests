from utils import run_tests, enable_tracing
import interp_Pvar
import interp_Lif
import interp_Ltup
import interp_Cif
import interp_Ctup
import interp_Lfun
import interp_Cfun
import type_check_Lfun
import type_check_Lvar
import type_check_Lif
import type_check_Cif
import type_check_Ltup
import type_check_Ctup
import type_check_Lfun
import type_check_Cfun
import sys
sys.path.append("..")
import compiler

sys.setrecursionlimit(10000)

compiler = compiler.Compiler()


enable_tracing()
if hasattr(compiler, "reveal_functions"):
    results = [
        run_tests("var", compiler, "var", type_check_Lfun.TypeCheckLfun().type_check, interp_Lfun.InterpLfun().interp, type_check_Cfun.TypeCheckCfun().type_check, interp_Cfun.InterpCfun().interp),
        run_tests("regalloc", compiler, "regalloc", type_check_Lfun.TypeCheckLfun().type_check, interp_Lfun.InterpLfun().interp, type_check_Cfun.TypeCheckCfun().type_check, interp_Cfun.InterpCfun().interp), 
        run_tests("lif", compiler, "lif", type_check_Lfun.TypeCheckLfun().type_check, interp_Lfun.InterpLfun().interp, type_check_Cfun.TypeCheckCfun().type_check, interp_Cfun.InterpCfun().interp), 
        run_tests("tuples", compiler, "tuples", type_check_Lfun.TypeCheckLfun().type_check, interp_Lfun.InterpLfun().interp, type_check_Cfun.TypeCheckCfun().type_check, interp_Cfun.InterpCfun().interp),
        run_tests("fun", compiler, "fun", type_check_Lfun.TypeCheckLfun().type_check, interp_Lfun.InterpLfun().interp, type_check_Cfun.TypeCheckCfun().type_check, interp_Cfun.InterpCfun().interp)
    ]
else:
    results = [run_tests("var", compiler, "var", type_check_Lif.TypeCheckLif().type_check, interp_Pvar.InterpPvar().interp_P, type_check_Cif.TypeCheckCif().type_check, interp_Cif.InterpCif().interp)]
    if hasattr(compiler, "allocate_registers"):
        results.append(run_tests("regalloc", compiler, "regalloc", type_check_Lif.TypeCheckLif().type_check, interp_Pvar.InterpPvar().interp_P, type_check_Cif.TypeCheckCif().type_check, interp_Cif.InterpCif().interp))
    if hasattr(compiler, "shrink"):
        results.append(run_tests("lif", compiler, "lif", type_check_Lif.TypeCheckLif().type_check, interp_Lif.InterpLif().interp, type_check_Cif.TypeCheckCif().type_check, interp_Cif.InterpCif().interp))
    if hasattr(compiler, "expose_allocation"):
        results.append(run_tests("tuples", compiler, "tuples", type_check_Ltup.TypeCheckLtup().type_check, interp_Ltup.InterpLtup().interp, type_check_Ctup.TypeCheckCtup().type_check, interp_Ctup.InterpCtup().interp))

if all(results):
    print("ALL TESTS PASSED! :D")
