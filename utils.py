import os
import sys
from sys import platform
import ast
from ast import *
from dataclasses import dataclass
from typing import Callable
from filecmp import cmp

################################################################################
# repr for classes in the ast module
################################################################################

indent_amount = 2


def indent_stmt():
    return " " * indent_amount

def indent():
    global indent_amount
    indent_amount += 2

def dedent():
    global indent_amount
    indent_amount -= 2

def str_Module(self):
    indent()
    body = ''.join([str(s) for s in self.body])
    dedent()
    return body
Module.__str__ = str_Module
def repr_Module(self):
    return 'Module(' + repr(self.body) + ')'
Module.__repr__ = repr_Module

def str_Expr(self):
    return indent_stmt() + str(self.value) + '\n'
Expr.__str__ = str_Expr
def repr_Expr(self):
    return indent_stmt() + 'Expr(' + repr(self.value) + ')'
Expr.__repr__ = repr_Expr

def str_Assign(self):
    return indent_stmt() + str(self.targets[0]) + ' = ' + str(self.value) + '\n'
Assign.__str__ = str_Assign
def repr_Assign(self):
    return indent_stmt() + 'Assign(' + repr(self.targets) + ', ' + repr(self.value) + ')'
Assign.__repr__ = repr_Assign

def str_AnnAssign(self):
    return indent_stmt() + str(self.target) + ' : ' + str(self.annotation) + ' = ' + str(self.value) + '\n'
AnnAssign.__str__ = str_AnnAssign
def repr_AnnAssign(self):
    return indent_stmt() + 'AnnAssign(' + repr(self.target) + ', ' \
        + repr(self.annotation) + ', ' + repr(self.value) + ')'
AnnAssign.__repr__ = repr_AnnAssign

def str_Return(self):
    return indent_stmt() + 'return ' + str(self.value) + '\n'
Return.__str__ = str_Return
def repr_Return(self):
    return indent_stmt() + 'Return(' + repr(self.value) + ')'
Return.__repr__ = repr_Return

def str_Name(self):
    return self.id
Name.__str__ = str_Name
def repr_Name(self):
    return 'Name(' + repr(self.id) + ')'
Name.__repr__ = repr_Name

def str_Constant(self):
    return str(self.value)
Constant.__str__ = str_Constant
def repr_Constant(self):
    return 'Constant(' + repr(self.value) + ')'
Constant.__repr__ = repr_Constant

supported_ops = [(Add, '+', 'Add()')
                ,(Sub, '-', 'Sub()')
                ,(Mult, '*', 'Mult()')
                ,(FloorDiv, '//', 'FloorDiv()')
                ,(Mod, '%', 'Mod()')
                ,(And, 'and', 'And()')
                ,(Or, 'or', 'Or()')
                ,(USub, '-', 'USub()')
                ,(Not, 'not', 'Not()')]

for op_cls, op_name, op_ast_name in supported_ops:
    op_cls.__str__  = (lambda op_name: lambda self: op_name) (op_name)
    op_cls.__repr__ = (lambda op_ast_name: lambda self: op_ast_name) (op_ast_name)

def str_BinOp(self):
    return '(' + str(self.left) + ' ' + str(self.op) + ' ' + str(self.right) + ')'
BinOp.__str__ = str_BinOp
def repr_BinOp(self):
    return 'BinOp(' + repr(self.left) + ', ' + repr(self.op) + ', ' + repr(self.right) + ')'
BinOp.__repr__ = repr_BinOp

def str_BoolOp(self):
    return '(' + str(self.values[0]) + ' ' + str(self.op) + ' ' + str(self.values[1]) + ')'
BoolOp.__str__ = str_BoolOp
def repr_BoolOp(self):
    return repr(self.values[0]) + ' ' + repr(self.op) + ' ' + repr(self.values[1])
BoolOp.__repr__ = repr_BoolOp

def str_UnaryOp(self):
    return str(self.op) + ' ' + str(self.operand)
UnaryOp.__str__ = str_UnaryOp
def repr_UnaryOp(self):
    return 'UnaryOp(' + repr(self.op) + ', ' + repr(self.operand) + ')'
UnaryOp.__repr__ = repr_UnaryOp

def str_Call(self):
    return str(self.func) + '(' + ', '.join([str(arg) for arg in self.args]) + ')'
Call.__str__ = str_Call
def repr_Call(self):
    return 'Call(' + repr(self.func) + ', ' + repr(self.args) + ')'
Call.__repr__ = repr_Call

def str_If(self):
    header = indent_stmt() + 'if ' + str(self.test) + ':\n'
    indent()
    thn = ''.join(str(s) for s in self.body)
    els = ''.join(str(s) for s in self.orelse)
    dedent()
    return header  + thn + indent_stmt() + 'else:\n' + els
If.__str__ = str_If
def repr_If(self):
    return 'If(' + repr(self.test) + ', ' + repr(self.body) + ', ' + repr(self.orelse) + ')'
If.__repr__ = repr_If

def str_IfExp(self):
    return '(' + str(self.body) + ' if ' + str(self.test) + ' else ' + str(self.orelse) + ')'
IfExp.__str__ = str_IfExp
def repr_IfExp(self):
    return 'IfExp(' + repr(self.body) + ', ' + repr(self.test) + ', ' + repr(self.orelse) + ')'
IfExp.__repr__ = repr_IfExp

def str_While(self):
    header = indent_stmt() + 'while ' + str(self.test) + ':\n'
    indent()
    body = ''.join(str(s) for s in self.body)
    dedent()
    return header + body
While.__str__ = str_While
def repr_While(self):
    return 'While(' + repr(self.test) + ', ' + repr(self.body) + ', ' + repr(self.orelse) + ')'
While.__repr__ = repr_While

def str_Compare(self):
    return str(self.left) + ' ' + str(self.ops[0]) + ' ' + str(self.comparators[0])
Compare.__str__ = str_Compare
def repr_Compare(self):
    return 'Compare(' + repr(self.left) + ', ' + repr(self.ops) + ', ' + repr(self.comparators) + ')'
Compare.__repr__ = repr_Compare

def str_Eq(self):
    return '=='
Eq.__str__ = str_Eq
def repr_Eq(self):
    return 'Eq()'
Eq.__repr__ = repr_Eq

def str_NotEq(self):
    return '!='
NotEq.__str__ = str_NotEq
def repr_NotEq(self):
    return 'NotEq()'
NotEq.__repr__ = repr_NotEq

def str_Lt(self):
    return '<'
Lt.__str__ = str_Lt
def repr_Lt(self):
    return 'Lt()'
Lt.__repr__ = repr_Lt

def str_LtE(self):
    return '<='
LtE.__str__ = str_Lt
def repr_LtE(self):
    return 'LtE()'
LtE.__repr__ = repr_LtE

def str_Gt(self):
    return '>'
Gt.__str__ = str_Gt
def repr_Gt(self):
    return 'Gt()'
Gt.__repr__ = repr_Gt

def str_GtE(self):
    return '>='
GtE.__str__ = str_GtE
def repr_GtE(self):
    return 'GtE()'
GtE.__repr__ = repr_GtE

def str_Tuple(self):
    return '(' + ', '.join(str(e) for e in self.elts)  + ',)'
Tuple.__str__ = str_Tuple
def repr_Tuple(self):
    return 'Tuple(' + repr(self.elts) + ')'
Tuple.__repr__ = repr_Tuple

def str_Subscript(self):
    return str(self.value) + '[' + str(self.slice) + ']'
Subscript.__str__ = str_Subscript
def repr_Subscript(self):
    return 'Subscript(' + repr(self.value) + ', ' + repr(self.slice) + ', ' + repr(self.ctx) + ')'
Subscript.__repr__ = repr_Subscript


def str_FunctionDef(self):
    if isinstance(self.args, ast.arguments):
        params = ', '.join(a.arg + ':' + str(a.annotation) for a in self.args.args)
    else:
        params = ', '.join(x + ':' + str(t) for (x,t) in self.args)
    indent()
    if isinstance(self.body, list):
        body = ''.join(str(s) for s in self.body)
    elif isinstance(self.body, dict):
        body = ''
        for (l,ss) in self.body.items():
            body += l + ':\n'
            indent()
            body += ''.join(str(s) for s in ss)
            dedent()
    dedent()
    return indent_stmt() + 'def ' + self.name + '(' + params + ')' + \
        ' -> ' + str(self.returns) + ':\n' + body + '\n'
def repr_FunctionDef(self):
    return 'FunctionDef(' + self.name + ',' + repr(self.args) + ',' + \
        repr(self.body) + ')'
FunctionDef.__str__ = str_FunctionDef
FunctionDef.__repr__ = repr_FunctionDef

def str_Lambda(self):
    if isinstance(self.args, ast.arguments):
        params = ', '.join(a.arg for a in self.args.args)
    else:
        params = ', '.join(self.args)
    body = str(self.body)
    return '(lambda ' + params + ': ' + body + ')'
def repr_Lambda(self):
    return 'Lambda(' + repr(self.args) + ',' + repr(self.body) + ')'
Lambda.__str__ = str_Lambda
Lambda.__repr__ = repr_Lambda
    

################################################################################
# __eq__ and __hash__ for classes in the ast module
################################################################################

def eq_Name(self, other):
    if isinstance(other, Name):
        return self.id == other.id
    else:
        return False
Name.__eq__ = eq_Name

def hash_Name(self):
    return hash(self.id)
Name.__hash__ = hash_Name

################################################################################
# map compare operators to their encoding
# could be done as a dictionary, but there is neither __hash__ nor __eq__
################################################################################

def cmp_to_code(cmp) -> str:
    match cmp:
        case Eq(): return 'e'
        case NotEq(): return 'ne'
        case Lt(): return 'l'
        case LtE(): return 'le'
        case Gt(): return 'g'
        case GtE(): return 'ge'

################################################################################
# Generating unique names
################################################################################

name_id = 0

def generate_name(name):
    global name_id
    ls = name.split('.')
    new_id = name_id
    name_id += 1
    return ls[0] + '.' + str(new_id)


################################################################################
# AST classes
################################################################################

Binding = tuple[Name, expr]
Temporaries = list[Binding]

class Type:
    pass

# Obsolete, use Begin instead. -Jeremy
# @dataclass
# class Let(expr):
#     var : expr
#     rhs : expr
#     body : expr

#     def __str__(self):
#         return '(let ' + str(self.var) + ' = ' + str(self.rhs) + ' in ' \
#             + str(self.body) + ')'

# Obsolete, use Begin instead. -Jeremy
# def make_lets(bs: Temporaries, e: expr) -> expr:
#     result = e
#     for (x,rhs) in reversed(bs):
#         result = Let(x, rhs, result)
#     return result

def make_assigns(bs: Temporaries) -> list[stmt]:
    return [Assign([x], rhs) for (x,rhs) in bs]

def make_begin(bs: Temporaries, e: expr) -> expr:
    if len(bs) > 0:
        return Begin(make_assigns(bs), e)
    else:
        return e

# A lambda expression whose parameters are annotated with types.
@dataclass
class AnnLambda(expr):
    params : list[tuple[str,Type]]
    returns : Type
    body : expr
    def __str__(self):
        return 'lambda [' + \
            ', '.join([x + ':' + str(t) for (x,t) in self.params]) + '] -> ' \
            + str(self.returns) + ': ' + str(self.body)

# An uninitialized value of a given type.
# Needed for boxing local variables.
@dataclass
class Uninitialized(expr):
    ty : Type
    def __str__(self):
        return 'uninit[' + str(self.ty) + ']'
    
@dataclass
class CProgram:
    body : list[stmt]

    def __str__(self):
        result = ''
        for (l,ss) in self.body.items():
            result += l + ':\n'
            indent()
            result += ''.join([str(s) for s in ss]) + '\n'
            dedent()
        return result

@dataclass
class CProgramDefs:
    defs : list[stmt]
    def __str__(self):
        return '\n'.join([str(d) for d in self.defs]) + '\n'
    
@dataclass
class Goto(stmt):
    label : str
    def __str__(self):
        return indent_stmt() + 'goto ' + self.label + '\n'

@dataclass
class Allocate(expr):
    length : int
    ty : Type
    def __str__(self):
        return 'allocate(' + str(self.length) + ',' + str(self.ty) + ')'

@dataclass
class AllocateClosure(expr):
    length : int
    ty : Type
    arity : int
    def __str__(self):
        return 'alloc_clos(' + str(self.length) + ',' + str(self.ty) \
            + ','  + str(self.arity) + ')'

@dataclass
class AllocateArray(expr):
    length : expr
    ty : Type
    def __str__(self):
        return 'alloc_array(' + str(self.length) + ',' + str(self.ty) + ')'

@dataclass
class Collect(stmt):
    size : int
    def __str__(self):
        return indent_stmt() + 'collect(' + str(self.size) + ')\n'

@dataclass
class CollectArray(stmt):
    size : expr
    def __str__(self):
        return indent_stmt() + 'collect_array(' + str(self.size) + ')\n'
    
@dataclass
class Begin(expr):
    body : list[stmt]
    result : expr
    def __str__(self):
        indent()
        stmts = ''.join([str(s) for s in self.body])
        end = indent_stmt() + 'produce ' + str(self.result)
        dedent()
        return '{\n' + stmts + end + '}'

@dataclass
class GlobalValue(expr):
    name : str
    def __str__(self):
        return str(self.name)

@dataclass(eq=True)
class IntType(Type):
    def __str__(self):
        return 'int'

@dataclass(eq=True)
class BoolType(Type):
    def __str__(self):
        return 'bool'

@dataclass(eq=True)
class VoidType(Type):
    def __str__(self):
        return 'void'
    
@dataclass(eq=True)
class Bottom(Type):
    def __str__(self):
        return 'bottom'

@dataclass(eq=True)
class TupleType(Type):
    types : list[Type]
    def __str__(self):
        return 'tuple[' + ','.join(map(str, self.types)) + ']'

@dataclass(eq=True)
class FunctionType:
    param_types : list[Type]
    ret_type : Type
    def __str__(self):
        return 'Callable[[' + ','.join(map(str, self.param_types))+']'\
            + ', ' + str(self.ret_type) + ']'

@dataclass(eq=True)
class ListType(Type):
    elt_ty : Type
    def __str__(self):
        return 'list[' + str(self.elt_ty) + ']'
    
@dataclass
class FunRef(expr):
    name : str
    arity : int
    def __str__(self):
        return '{' + self.name + '}'
    
@dataclass
class TailCall(stmt):
    func : expr
    args : list[expr]
    def __str__(self):
        return indent_stmt() + 'tail ' + str(self.func) + '(' + ', '.join([str(e) for e in self.args]) + ')\n'

# like a Tuple, but also stores the function's arity
@dataclass
class Closure(expr):
    arity : int
    args : list[expr]
    __match_args__ = ("arity", "args")
    def __str__(self):
        return 'closure[' + repr(self.arity) + '](' + ', '.join([str(e) for e in self.args]) + ')'

@dataclass
class Inject(expr):
    value : expr
    typ : Type
    __match_args__ = ("value", "typ")
    def __str__(self):
        return 'inject(' + str(self.value) + ', ' + str(self.typ) + ')'

@dataclass
class Project(expr):
    value : expr
    typ : Type
    __match_args__ = ("value", "typ")
    def __str__(self):
        return 'project(' + str(self.value) + ', ' + str(self.typ) + ')'
    
@dataclass
class TagOf(expr):
    value : expr
    __match_args__ = ("value",)
    def __str__(self):
        return 'tagof(' + str(self.value) + ')'

@dataclass
class ValueOf(expr):
    value : expr
    typ : Type
    __match_args__ = ("value","typ")
    def __str__(self):
        return 'valueof(' + str(self.value) + ', ' + str(self.typ) + ')'
    
@dataclass(eq=True)
class AnyType(Type):
    def __str__(self):
        return 'any'

# Base class of runtime values
class Value:
    pass

block_id = 0

def create_block(stmts: list[stmt], basic_blocks:dict[str,list[stmt]]) -> Goto:
    'stuff statments into a new basic block; return a jump to it'
    global block_id
    label = 'block' + str(block_id)
    block_id += 1
    basic_blocks[label_name(label)] = stmts
    return Goto(label)
    
################################################################################
# Miscellaneous Auxiliary Functions
################################################################################

def input_int() -> int:
    return int(input())


def unzip(ls):
    xs, ys = [], []
    for (x, y) in ls:
        xs += [x]
        ys += [y]
    return (xs, ys)


def align(n: int, alignment: int) -> int:
    if 0 == n % alignment:
        return n
    else:
        return n + (alignment - n % alignment)

def bool2int(b):
    if b:
        return 1
    else:
        return 0

label_name: Callable[[str], str] = (lambda n: '_' + n) if platform == 'darwin' else (lambda n: n)

# def label_name(n: str) -> str:
#     if platform == "darwin":
#         return '_' + n
#     else:
#         return n
    
tracing = False

def enable_tracing():
    global tracing
    tracing = True

def trace(msg):
    if tracing:
        print(msg, file=sys.stderr)

def is_python_extension(filename):
    s = filename.split(".")
    if len(s) > 1:
        return s[1] == "py"
    else:
        return False

def ensure_final_newline(filename):
    # check whether file is empty
    if os.stat(filename).st_size != 0:
        with open(filename, "r+b") as f:
            # must open as b to seek from end; read last character
            f.seek(-1, 2)
            b = f.read(1)
            newline = bytes('\n', 'utf-8')
            if b != newline:
                f.write(newline)


compare_files = lambda file1, file2: cmp(file1, file2, shallow=False)


# Given the `ast` output of a pass and a test program (root) name,
# runs the interpreter on the program and compares the output to the
# expected "golden" output.
def test_pass(passname, interp, program_root, ast, compiler_name) -> bool:
    input_file = program_root + ".in"
    output_file = program_root + ".out"
    stdin = sys.stdin
    stdout = sys.stdout
    sys.stdin = open(input_file, "r")
    sys.stdout = open(output_file, "w")
    interp(ast)
    sys.stdin = stdin
    sys.stdout = stdout
    ensure_final_newline(program_root + '.out')
    ensure_final_newline(program_root + '.golden')
    result = compare_files(output_file, program_root + ".golden")
    if result:
        trace(
            "compiler "
            + compiler_name
            + " success on pass "
            + passname
            + " on test\n"
            + program_root
            + "\n"
        )
        return 1
    else:
        print(
            "compiler "
            + compiler_name
            + " failed pass "
            + passname
            + " on test\n"
            + program_root
            + "\n"
        )
        output = open(program_root + ".out").read()
        expected = open(program_root + ".golden").read()
        print("Output: " + output)
        print("Expected: "+ expected)
        return 0


def validate_tests(lang: str, interp) -> bool:
    '''check if all tests for `lang` work with `interp`'''
    test_count = 0
    success_count = 0
    tests = get_all_tests_for(lang)
    for test_filename in tests:
        program_root = test_filename.split('.')[0]
        with open(test_filename) as source:
            program = parse(source.read())
        test_count += 1
        success_count += test_pass('--', interp, program_root, program, lang)
    return test_count == success_count


def compile_and_test(
    compiler,
    compiler_name,
    type_check_P,
    interp_P,
    type_check_C,
    interp_C,
    program_filename,
):
    def execute_pass(passname: str, program, interp= interp_P, type_check= None):
        nonlocal total_passes, successful_passes
        if hasattr(compiler, passname):
            trace('\n#' + passname + '\n')
            if type_check:
                type_check(program)
            program_out = getattr(compiler, passname)(program)
            trace(program_out)
            trace('')
            total_passes += 1
            successful_passes += test_pass(
                passname, interp, program_root, program_out, compiler_name
            )
        else:
            program_out = program
        return program_out

    total_passes = 0
    successful_passes = 0
    from interp_x86.eval_x86 import interp_x86

    program_root = program_filename.split('.')[0]
    with open(program_filename) as source:
        program = parse(source.read())

    trace('\n# source program\n')
    trace(program)
    trace('')

    program = execute_pass('shrink', program)
    program = execute_pass('reveal_functions', program, type_check= type_check_P)
    program = execute_pass('limit_functions', program, type_check= type_check_P)
    program = execute_pass('resolve', program, type_check= type_check_P)
    program = execute_pass('check_bounds', program, type_check= type_check_P)
    program = execute_pass('expose_allocation', program, type_check= type_check_P)
    program = execute_pass('remove_complex_operands', program)
    program = execute_pass('explicate_control', program, interp= interp_C)

    if type_check_C:
        trace("\n**********\n type check C \n**********\n")
        type_check_C(program)

    trace("\n**********\n select \n**********\n")
    pseudo_x86 = compiler.select_instructions(program)
    trace(pseudo_x86)
    trace("")
    total_passes += 1
    test_x86 = False # doesn't know about GC!
    if test_x86:
        successful_passes += test_pass(
            "select instructions", interp_x86, program_root, pseudo_x86, compiler_name
        )

    trace("\n**********\n assign \n**********\n")
    almost_x86 = compiler.assign_homes(pseudo_x86)
    trace(almost_x86)
    trace("")
    total_passes += 1
    if test_x86:
        successful_passes += test_pass(
            "assign homes", interp_x86, program_root, almost_x86, compiler_name
        )

    trace("\n**********\n patch \n**********\n")
    x86 = compiler.patch_instructions(almost_x86)
    trace(x86)
    trace("")
    total_passes += 1
    if test_x86:
        successful_passes += test_pass(
            "patch instructions", interp_x86, program_root, x86, compiler_name
        )

    trace('\n# prelude and conclusion\n')
    final_program = compiler.prelude_and_conclusion(x86)
    trace(final_program)
    trace("")
    
    x86_filename = program_root + ".s"
    with open(x86_filename, "w") as dest:
        dest.write(str(final_program))
        
    total_passes += 1
        
    # Run the final x86 program
    emulate_x86 = False
    if emulate_x86:
        stdin = sys.stdin
        stdout = sys.stdout
        sys.stdin = open(program_root + '.in', 'r')
        sys.stdout = open(program_root + '.out', 'w')
        interp_x86(final_program)
        sys.stdin = stdin
        sys.stdout = stdout
    else:
        os.system('gcc runtime.o ' + x86_filename)
        input_file = program_root + '.in'
        output_file = program_root + '.out'
        os.system('./a.out < ' + input_file + ' > ' + output_file)

    ensure_final_newline(program_root + '.out')
    ensure_final_newline(program_root + '.golden')
    result = compare_files(program_root + ".out", program_root + ".golden")
    if result:
        successful_passes += 1
        return (successful_passes, total_passes, 1)
    else:
        print('compiler ' + compiler_name + ', executable failed' \
              + ' on test ' + program_root)
        return (successful_passes, total_passes, 0)

def trace_ast_and_concrete(ast):
    trace("concrete syntax:")
    trace(ast)
    trace("")
    trace("AST:")
    trace(repr(ast))    
    
# This function compiles the program without any testing
def compile(compiler, compiler_name, type_check_P, type_check_C,
            program_filename):
    program_root = program_filename.split('.')[0]
    with open(program_filename) as source:
        program = parse(source.read())

    trace('\n# type check\n')        
    type_check_P(program)
    trace_ast_and_concrete(program)
        
    if hasattr(compiler, 'shrink'):
        trace('\n# shrink\n')
        program = compiler.shrink(program)
        trace_ast_and_concrete(program)

    if hasattr(compiler, 'uniquify'):
        trace('\n# uniquify\n')
        program = compiler.uniquify(program)
        trace_ast_and_concrete(program)
        
    if hasattr(compiler, 'reveal_functions'):
        trace('\n# reveal functions\n')
        type_check_P(program)
        program = compiler.reveal_functions(program)
        trace_ast_and_concrete(program)

    if hasattr(compiler, 'convert_assignments'):
        trace('\n# assignment conversion\n')
        type_check_P(program)
        program = compiler.convert_assignments(program)
        trace_ast_and_concrete(program)
        
    if hasattr(compiler, 'convert_to_closures'):
        trace('\n# closure conversion\n')
        type_check_P(program)
        program = compiler.convert_to_closures(program)
        trace_ast_and_concrete(program)
        
    if hasattr(compiler, 'expose_allocation'):
        trace('\n# expose allocation\n')
        type_check_P(program)
        program = compiler.expose_allocation(program)
        trace_ast_and_concrete(program)
        
    trace('\n# remove complex\n')
    program = compiler.remove_complex_operands(program)
    trace_ast_and_concrete(program)
    
    if hasattr(compiler, 'explicate_control'):
        trace('\n# explicate control\n')
        program = compiler.explicate_control(program)
        trace_ast_and_concrete(program)

    if type_check_C:
        type_check_C(program)
        
    trace('\n# select instructions\n')    
    pseudo_x86 = compiler.select_instructions(program)
    trace_ast_and_concrete(pseudo_x86)
    
    trace('\n# assign homes\n')    
    almost_x86 = compiler.assign_homes(pseudo_x86)
    trace_ast_and_concrete(almost_x86)
    
    trace('\n# patch instructions\n')        
    x86 = compiler.patch_instructions(almost_x86)
    trace_ast_and_concrete(x86)

    trace('\n# prelude and conclusion\n')
    x86 = compiler.prelude_and_conclusion(x86)
    trace_ast_and_concrete(x86)
    
    # Output x86 program to the .s file
    x86_filename = program_root + ".s"
    with open(x86_filename, "w") as dest:
        dest.write(str(x86))        
    

# Given a test file name, the name of a language, a compiler, a type
# checker and interpreter for the language, and an interpeter for the
# C intermediate language, run all the passes in the compiler,
# checking that the resulting programs produce output that matches the
# golden file.
def run_one_test(
    test, lang, compiler, compiler_name, type_check_P, interp_P, type_check_C, interp_C
):
    # test_root = test.split(".")[0]
    # test_name = test_root.split("/")[-1]
    return compile_and_test(
        compiler, compiler_name, type_check_P, interp_P, type_check_C, interp_C, test
    )


# Given the name of a language, a compiler, the compiler's name, a
# type checker and interpreter for the language, and an interpreter
# for the C intermediate language, test the compiler on all the tests
# in the directory of for the given language, i.e., all the
# python files in ./tests/<language>.
def run_tests(
    lang, compiler, compiler_name, type_check_P, interp_P, type_check_C, interp_C
):
    tests = get_all_tests_for(lang)

    # Compile and run each test program, comparing output to the golden file.
    successful_passes = 0
    total_passes = 0
    successful_tests = 0
    total_tests = 0
    for test in tests:
        (succ_passes, tot_passes, succ_test) = run_one_test(
            test,
            lang,
            compiler,
            compiler_name,
            type_check_P,
            interp_P,
            type_check_C,
            interp_C,
        )
        successful_passes += succ_passes
        total_passes += tot_passes
        successful_tests += succ_test
        total_tests += 1

    # Report the pass/fails
    print('tests: ' + repr(successful_tests) + '/' + repr(total_tests) \
          + ' for compiler ' + compiler_name + ' on language ' + lang)
    print('passes: ' + repr(successful_passes) + '/' + repr(total_passes) \
          + ' for compiler ' + compiler_name + ' on language ' + lang)

    if successful_tests == total_tests:
        return True
    return False

def get_all_tests_for(lang):
    '''Collect all the test program file names for language `lang`.'''
    homedir = os.getcwd()
    directory = homedir + '/' + lang + '/'
    if not os.path.isdir(directory):
        raise Exception('missing directory for test programs: ' \
                        + directory)
    (dirpath, dirnames, filenames) = next(os.walk(directory))
    tests = [dirpath + t for t in filenames if is_python_extension(t)]
    return tests
