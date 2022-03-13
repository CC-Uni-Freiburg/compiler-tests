from ast import *
import math
from interp_Lfun import InterpLfun
from utils import *

class InterpLexam(InterpLfun):

  def interp_exp(self, e, env):
    match e:
      case List(es, Load()):
        return [self.interp_exp(e, env) for e in es]
      case BinOp(left, Mult(), right):
          l = self.interp_exp(left, env); r = self.interp_exp(right, env)
          return l * r
      case BinOp(left, FloorDiv(), right):
          l = self.interp_exp(left, env); r = self.interp_exp(right, env)
          aq = abs(l) // abs(r)
          return aq if l * r >=0 else -aq
      case BinOp(left, Mod(), right):
          l = self.interp_exp(left, env); r = self.interp_exp(right, env)
          ar = abs(l) % abs(r)
          return ar if l >=0 else -ar
      case Call(Name('array_len'), [tup]):
        t = self.interp_exp(tup, env)
        return len(t)
      case Call(Name('array_load'), [tup, index]):
        t = self.interp_exp(tup, env)
        i = self.interp_exp(index, env)
        return t[i]
      case Call(Name('array_store'), [tup, index, value]):
        t = self.interp_exp(tup, env)
        i = self.interp_exp(index, env)
        v = self.interp_exp(value, env)
        t[i] = v
        return None
      case _:
        return super().interp_exp(e, env)

  def interp_stmts(self, ss, env):
    if len(ss) == 0:
      return
    match ss[0]:
      case Assign([Subscript(lst, index)], value):
        lst = self.interp_exp(lst, env)
        index = self.interp_exp(index, env)
        if index < 0:
            raise IndexError('less than zero')
        lst[index] = self.interp_exp(value, env)
        return self.interp_stmts(ss[1:], env)
      case _:
        return super().interp_stmts(ss, env)
