from utils import enable_tracing, run_tests
import sys
sys.path.insert(0, "..")
from compiler_Lexam import CompilerLexam
from type_check_Lexam import TypeCheckLexam
from interp_Lexam import InterpLexam
from type_check_Cexam import TypeCheckCexam
from interp_Cexam import InterpCexam

sys.setrecursionlimit(10000)

compiler = CompilerLexam()

enable_tracing()

test_suites = ['exam']

passed = True

for test_suite in test_suites:
    res = run_tests(test_suite, compiler, "exam",
            TypeCheckLexam().type_check,
            InterpLexam().interp,
            TypeCheckCexam().type_check,
            InterpCexam().interp)
    if not res:
        passed = False

if passed:
    print("All tests passed!")
